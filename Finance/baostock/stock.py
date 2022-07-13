#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time
from multiprocessing import  Process
import baostock as bs
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import DATE, CHAR, VARCHAR, INT, DECIMAL, Float, FLOAT

DB = "STK"
DB_HOST = "192.168.31.27"
DB_USER = "root"
DB_PWD = "123456"
MySQL_Engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB}')

# 获取行业分类数据
def stock_industry_proc():
    rs = bs.query_stock_industry()

    if rs.error_code != '0':
        print("query stock industry failed!")
        print("error code:" + rs.error_code + "error msg:" + rs.error_msg)
        return;

    data = rs.get_data()
    DTYPES = {'updateDate':CHAR(10), 'code':CHAR(9), 'code_name':VARCHAR(16), 'industry':VARCHAR(16), 'industryClassification':VARCHAR(32)}
    data.to_sql("stock_industry", con=MySQL_Engine, if_exists="replace", index=False, dtype=DTYPES)
    with MySQL_Engine.connect() as con:
        con.execute(f"ALTER TABLE {DB}.stock_industry MODIFY COLUMN updateDate char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.stock_industry MODIFY COLUMN code char(9) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.stock_industry MODIFY COLUMN code_name varchar(16) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.stock_industry ADD CONSTRAINT stock_industry_PK PRIMARY KEY (code);")

# 获取上证50成分股
def sz50_stocks_proc():
    rs = bs.query_sz50_stocks()
    if rs.error_code != '0':
        print("query sz50 stocks failed!")
        print("error code:" + rs.error_code + "error msg:" + rs.error_msg)
        return;

    data = rs.get_data()
    DTYPES = {'updateDate': CHAR(10), 'code': CHAR(9), 'code_name': VARCHAR(16)}
    data.to_sql("sz50_stock", con=MySQL_Engine, if_exists="replace", index=False, dtype=DTYPES)
    with MySQL_Engine.connect() as con:
        con.execute(f"ALTER TABLE {DB}.sz50_stock MODIFY COLUMN updateDate char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.sz50_stock MODIFY COLUMN code char(9) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.sz50_stock MODIFY COLUMN code_name varchar(16) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.sz50_stock ADD CONSTRAINT sz50_stock_PK PRIMARY KEY (code);")

# 获取沪深300成分股
def hs300_stocks_proc():
    rs = bs.query_hs300_stocks()
    if rs.error_code != '0':
        print("query hs300 stocks failed!")
        print("error code:" + rs.error_code + "error msg:" + rs.error_msg)
        return;

    data = rs.get_data()
    DTYPES = {'updateDate': CHAR(10), 'code': CHAR(9), 'code_name': VARCHAR(16)}
    data.to_sql("hs300_stock", con=MySQL_Engine, if_exists="replace", index=False, dtype=DTYPES)
    with MySQL_Engine.connect() as con:
        con.execute(
            f"ALTER TABLE {DB}.hs300_stock MODIFY COLUMN updateDate char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(
            f"ALTER TABLE {DB}.hs300_stock MODIFY COLUMN code char(9) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(
            f"ALTER TABLE {DB}.hs300_stock MODIFY COLUMN code_name varchar(16) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.hs300_stock ADD CONSTRAINT sz50_stock_PK PRIMARY KEY (code);")

# 获取中证500成分股
def zz500_stocks_proc():
    rs = bs.query_zz500_stocks()
    if rs.error_code != '0':
        print("query zz500 stocks failed!")
        print("error code:" + rs.error_code + "error msg:" + rs.error_msg)
        return;

    data = rs.get_data()
    DTYPES = {'updateDate': CHAR(10), 'code': CHAR(9), 'code_name': VARCHAR(16)}
    data.to_sql("zz500_stock", con=MySQL_Engine, if_exists="replace", index=False, dtype=DTYPES)
    with MySQL_Engine.connect() as con:
        con.execute(
            f"ALTER TABLE {DB}.zz500_stock MODIFY COLUMN updateDate char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(
            f"ALTER TABLE {DB}.zz500_stock MODIFY COLUMN code char(9) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(
            f"ALTER TABLE {DB}.zz500_stock MODIFY COLUMN code_name varchar(16) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.zz500_stock ADD CONSTRAINT sz50_stock_PK PRIMARY KEY (code);")

# 获取银行间同业拆放利率
def shibor_data_proc():
    # 2022-05-01  2022-06-05
    rs = bs.query_shibor_data(start_date="", end_date="")
    if rs.error_code != '0':
        print("query shibor data failed!")
        print("error code:" + rs.error_code + "error msg:" + rs.error_msg)
        return;

    data = rs.get_data()
    DTYPES = {'date': CHAR(10), 'shiborON': Float, 'shibor1W': Float, 'shibor2W': Float, 'shibor1M': Float,
              'shibor3M': Float, 'shibor6M': Float, 'shibor9M': Float, 'shibor1Y': Float}
    data.to_sql("shibor_data", con=MySQL_Engine, if_exists="replace", index=False, dtype=DTYPES)
    with MySQL_Engine.connect() as con:
        con.execute(f"ALTER TABLE {DB}.shibor_data MODIFY COLUMN `date` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.shibor_data ADD CONSTRAINT shibor_data_PK PRIMARY KEY (`date`);")

# 货币供应量(年底余额)
def money_supply_data_year_proc():
    rs = bs.query_money_supply_data_year()
    if rs.error_code != '0':
        print("query money supply data year data failed!")
        print("error code:" + rs.error_code + "error msg:" + rs.error_msg)
        return;

    data = rs.get_data()
    data = data.replace("", "0")
    DTYPES = {'statYear': CHAR(4), 'm0Year': Float, 'm0YearYOY': Float,
              'm1Year': Float, 'm1YearYOY': Float, 'm2Year': Float,
              'm2YearYOY': Float}
    data.to_sql("money_supply_data_year", con=MySQL_Engine, if_exists="replace", index=False, dtype=DTYPES)
    with MySQL_Engine.connect() as con:
        con.execute(f"ALTER TABLE {DB}.money_supply_data_year MODIFY COLUMN statYear char(4) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.money_supply_data_year ADD CONSTRAINT money_supply_data_year_PK PRIMARY KEY (statYear);")

# 货币供应量(月)
def money_supply_data_month_proc():
    rs = bs.query_money_supply_data_month()
    if rs.error_code != '0':
        print("query money supply data month data failed!")
        print("error code:" + rs.error_code + "error msg:" + rs.error_msg)
        return;

    data = rs.get_data()
    data = data.replace("", "0")
    DTYPES = {'statYear': CHAR(4), 'statMonth': CHAR(2), 'm0Month': Float, 'm0YOY': Float,
              'm0ChainRelative': Float, 'm1Month': Float, 'm1YOY': Float, 'm1ChainRelative': Float}
    data.to_sql("money_supply_data_month", con=MySQL_Engine, if_exists="replace", index=False, dtype=DTYPES)
    with MySQL_Engine.connect() as con:
        con.execute(f"ALTER TABLE {DB}.money_supply_data_month MODIFY COLUMN statYear char(4) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.money_supply_data_month MODIFY COLUMN statMonth char(2) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
        con.execute(f"ALTER TABLE {DB}.money_supply_data_month ADD CONSTRAINT money_supply_data_month_PK PRIMARY KEY (statYear,statMonth);")

# 证券基本资料
def stock_basic_proc():
    rs = bs.query_stock_basic()
    if rs.error_code != '0':
        print("query stock basic failed!")
        print("error code:" + rs.error_code + "error msg:" + rs.error_msg)
        return;

    data = rs.get_data()
    DTYPES = {'code': CHAR(9), 'code_name': VARCHAR(128), 'ipoDate': CHAR(10), 'outDate': CHAR(10), 'type': CHAR(1), 'status': CHAR(1)}
    data.to_sql("stock_basic", con=MySQL_Engine, if_exists="replace", index=False, dtype=DTYPES)

def stock_k_day_data_process(data, fields):
    klineD = data
    print("\tdata import to DB begin:", time.time())
    for key in klineD.keys():
        data = pd.DataFrame(klineD[key], columns=fields)
        data = data.replace("", "0")
        TableName = 'k_d_' + key;
        DTYPES = {'date': CHAR(10), 'code': CHAR(9), 'open': Float, 'high': Float, 'low': Float,
                  'close': Float, 'preclose': Float, 'volume': Float, 'amount': Float, 'adjustflag': CHAR(1),
                  'turn': Float, 'tradestatus': CHAR(1), 'pctChg': Float, 'peTTM': Float, 'psTTM': Float,
                  'pcfNcfTTM': Float, 'pbMRQ': Float, 'isST': CHAR(1)}
        data.to_sql(TableName, con=MySQL_Engine, if_exists="append", index=False, dtype=DTYPES, method='multi')
    print("\tdata import to DB end:", time.time())

# 获取K线数据（天）
def stock_k_day_data_proc():
    CCNT = 0
    with MySQL_Engine.connect() as con:
        res = con.execute(f"SELECT code FROM {DB}.stock_industry").all()
        for row in res:
            print(row, (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
            Fields = "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,psTTM,pcfNcfTTM,pbMRQ,isST"
            print("\tquery_history_k_data_plus begin", time.time())
            rs = bs.query_history_k_data_plus(code=row[0], fields=Fields, frequency='d', adjustflag='3', start_date="1990-01-01")
            print("\tquery_history_k_data_plus end", time.time())

            klineD = {}
            print("\tdata convert begin:", time.time())
            CNT = 0
            while (rs.error_code == '0') & rs.next():
                row = rs.get_row_data()
                CNT = CNT + 1
                year = row[0][:4]
                if year not in klineD:
                    klineD[year] = []
                klineD[year].append(row)
            print("\tdata convert end:", time.time(), " COUNT: ", CNT)

            p = Process(target=stock_k_day_data_process, args=(klineD,rs.fields,))
            p.start()
            # time.sleep(1)
            CCNT= CCNT + 1
            if CCNT % 100 == 0 :
                time.sleep(30)



                # if bAddPKey:
                #     bAddPKey = False
                #     with MySQL_Engine.connect() as con:
                #         con.execute(f"ALTER TABLE {DB}.k_d_1999 MODIFY COLUMN `date` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
                #         con.execute(f"ALTER TABLE {DB}.k_d_1999 MODIFY COLUMN code char(9) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;")
                #         con.execute(f"ALTER TABLE {DB}.k_d_1999 ADD CONSTRAINT k_d_1999_PK PRIMARY KEY (`date`,code);")

def MainProc():
    if False:
        print("stock_industry_proc...")
        stock_industry_proc()
        print("sz50_stocks_proc...")
        sz50_stocks_proc()
        print("hs300_stocks_proc...")
        hs300_stocks_proc()
        print("zz500_stocks_proc...")
        zz500_stocks_proc()
        print("shibor_data_proc...")
        shibor_data_proc()
        print("money_supply_data_year_proc...")
        money_supply_data_year_proc()
        print("money_supply_data_month_proc...")
        money_supply_data_month_proc()
        print("stock_basic_proc...")
        stock_basic_proc()

    print("stock_k_day_data_proc...")
    stock_k_day_data_proc()

if __name__ == "__main__":
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    if int(lg.error_code) == 0:
        print('login baostock successed!')
    elif int(lg.error_code) != 0:
        print('login baostock failed! error_code:'+lg.error_code + " error_msg:" + lg.error_msg)
        exit(-1)

    MainProc()

    bs.logout()
    exit(0)