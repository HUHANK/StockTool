#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/2319:03
# @File     : BaoStockService.py
# @Project  : Finance

import sqlalchemy
import baostock as bs
import datetime, time

DB = {}
# DB["Host"] = "121.89.165.101"
# DB['Port'] = 30006
# DB["User"] ="root"
# DB["Pwd"]  = "~Aa0903"
# DB["db"]   = "STK"

DB["Host"] = "172.31.114.22"
DB['Port'] = 3306
DB["User"] ="root"
DB["Pwd"]  = "123456"
DB["db"]   = "STK"

K_DATA_BEGIN_DATE = "2022-01-01"

MySQL = sqlalchemy.create_engine(f"mysql+pymysql://{DB['User']}:{DB['Pwd']}@{DB['Host']}:{DB['Port']}/{DB['db']}")

def stock_basic_proc() -> None:
    rs = bs.query_stock_basic()
    if rs.error_code != '0':
        print("query stock basic failed!")
        print("error code:" + rs.error_code + "error msg:" + rs.error_msg)
        return;

    data = rs.get_data()
    data.to_sql("stock_basic", con=MySQL, if_exists="replace", index=False)

    with MySQL.connect() as con:
        con.execute(f"ALTER TABLE {DB['db']}.stock_basic MODIFY COLUMN code char(10) NOT NULL;");
        con.execute(
            f"ALTER TABLE {DB['db']}.stock_basic MODIFY COLUMN code_name char(64) NULL;");
        con.execute(
            f"ALTER TABLE {DB['db']}.stock_basic MODIFY COLUMN ipoDate char(10) NULL;");
        con.execute(
            f"ALTER TABLE {DB['db']}.stock_basic MODIFY COLUMN outDate char(10) NULL;");
        con.execute(
            f"ALTER TABLE {DB['db']}.stock_basic MODIFY COLUMN `type` char(1) NULL;");
        con.execute(
            f"ALTER TABLE {DB['db']}.stock_basic MODIFY COLUMN status char(1) NULL;");
        con.execute(
            f"ALTER TABLE {DB['db']}.stock_basic ADD CONSTRAINT stock_basic_PK PRIMARY KEY (code);");

    for index, row in data.iterrows():
        if row['type'] in ',1,2,3,':
            print("--------------------")
            print(row['code'], row['type'])
            stock_kd_data_proc(row['code'], '1')
            stock_kd_data_proc(row['code'], '2')
            stock_kd_data_proc(row['code'], '3')

def stock_kd_data_proc(code, Adjustflag):
    Fields = "date,code,open,high,low," \
             "close,preclose,volume,amount,adjustflag," \
             "turn,tradestatus,pctChg,peTTM,psTTM," \
             "pcfNcfTTM,pbMRQ,isST"
    rs = bs.query_history_k_data_plus(code=code, fields=Fields,
            frequency='d', adjustflag=str(Adjustflag), start_date=K_DATA_BEGIN_DATE
            , end_date=str(datetime.date.today()))
    if rs is None:
        print("result is None.")
        return

    if rs.error_code != '0':
        print("query stock k data failed!")
        print("error code:" + rs.error_code + "error msg:" + rs.error_msg)
        return

    data = rs.get_data()
    sqls = []
    for index, row in data.iterrows():
        # print(row)
        sql = f"INSERT INTO {DB['db']}.k_d_{row['date'][0:4]} ({Fields}) VALUES (" \
              f"'{row['date']}', '{row['code']}', {row['open']}, {row['high']}, {row['low']}," \
              f"{row['close']}, {row['preclose']}, {row['volume']}, {row['amount']}, '{row['adjustflag']}'," \
              f"{row['turn']}, '{row['tradestatus']}', {row['pctChg']}, {row['peTTM']}, {row['psTTM']}," \
              f"{row['pcfNcfTTM']}, {row['pbMRQ']}, '{row['isST']}');"
        sqls.append(sql)

    print("SEC_CODE:", code, "COUNT:", len(sqls))

    with MySQL.connect() as con:
        for sql in sqls:
            try:
                con.execute(sql)
            except Exception as e:
                print(e)

def BaoStockDataProcess():
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    if int(lg.error_code) == 0:
        print('login baostock successed!')
    elif int(lg.error_code) != 0:
        print('login baostock failed! error_code:' + lg.error_code + " error_msg:" + lg.error_msg)
        return

    stock_basic_proc()
    bs.logout()
    return



if __name__ == "__main__":
    while True:
        curDate = str(datetime.date.today())
        if curDate != K_DATA_BEGIN_DATE:
            BaoStockDataProcess()
            K_DATA_BEGIN_DATE = curDate
        time.sleep(5)
    exit(0)