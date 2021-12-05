#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/23 20:32
# @Author : HuYouLiang
# @File : stock.py
# @Purpose :

from multiprocessing import Process, Queue, Lock
import  json
import pymysql
from common.network import *
import traceback


BStop = False
db = None
PLock = Lock()
AMOUNT = 0

def showAmount(cnt, lock):
    global AMOUNT
    with lock:
        AMOUNT = AMOUNT + cnt
        print("Current Process Count: %s"%AMOUNT)


def getklines(url, conn):
    result = wget(url)
    index1 = result.find('(')+1;
    index2 = result.rfind(')');
    js = json.loads(result[index1: index2])

    cursor = conn.cursor()
    ret = len(js["data"]["klines"])

    code = js["data"]["code"]
    COUNT = 0
    sql = "INSERT INTO kline(`index`, `code`, `date`, `open`, `high`, `close`, `low`, `amount`," \
          " `turnover`, `amplitude`, `p_change`, `price_change`, `exchange`) VALUES (" \
          "%s, %s,  %s, %s,   %s,   %s,    %s,   %s,   %s,        %s,         %s,       %s,          %s)"
    datas = []
    for line in js["data"]["klines"]:
        COUNT = COUNT + 1
        arr = line.split(",")
        #print(arr)
        date = arr[0].replace('-',"")
        # sql = "INSERT INTO kline(";
        # sql+= "`index`, `code`, `date`, `open`, `high`, `close`, `low`, `amount`, `turnover`, `amplitude`, `p_change`, `price_change`, `exchange`";
        # sql+= ") VALUES (" \
        #       "'%s', '%s',  '%s', %s,   %s,   %s,    %s,   %s,   %s,        %s,         %s,       %s,          %s);"%(
        #     date+code, code, date, arr[1], arr[3], arr[2], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10]
        # )
        row = []
        row.append(date+code)
        row.append(code)
        row.append(date)
        row.append(arr[1])
        row.append(arr[3])
        row.append(arr[2])
        row.append(arr[4])
        row.append(arr[5])
        row.append(arr[6])
        row.append(arr[7])
        row.append(arr[8])
        row.append(arr[9])
        row.append(arr[10])
        datas.append(row)

        if COUNT % 6000 == 0:
            res = cursor.executemany(sql, datas)
            print(res)
            conn.commit()
            datas.clear()
    res = cursor.executemany(sql, datas)
    print(res)
    conn.commit()
    cursor.close()
    return ret

def getStockData():
    sql = "SELECT * FROM sec_code;"
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)

    ret = cursor.fetchall()
    cursor.close()
    return ret

def genURL(data):
    URL = "http://66.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery112407407881261721598_1637762378256&secid={0}.{1}&ut=" \
          "fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2C" \
          "f58%2Cf59%2Cf60%2Cf61&klt=101&fqt=0&beg=0&end=20500101&smplmt={2}&lmt=1000000&_=1637762378257"
    for row in data:
        print(row)
        MarketCode = row["MARKET_CODE"]
        SecCode = row["SEC_CODE"]
        surl = URL.format(MarketCode, SecCode, 100000)
        #print(surl)
        MQUEUE.put(surl)
        #getklines(surl)



def MainProcess(queue, squeue, lock):
    print("MainProcess")
    conn = pymysql.connect(user='root', password='12345678', host='192.168.2.222', db='FINA')
    while True:
        try:
            url = queue.get()
            print(url)
            cnt = getklines(url, conn)
            #squeue.put(cnt)
        except:
            print(traceback.format_exc())

def ShowProcess(queue):
    ICNT = 0
    while True:
        cnt = queue.get()
        ICNT = ICNT + cnt
        print("Now Process Num: %s"%ICNT)

MQUEUE = Queue(20)
SQUEUE = Queue(100)
if __name__ == "__main__":
    db = pymysql.connect(user='root', password='12345678', host='192.168.2.222', db='FINA')

    processes = {}
    CNT = 20
    for i in range(CNT):
        processes[i] = Process(target=MainProcess, args=(MQUEUE, SQUEUE, PLock, ))
        processes[i].start()

    genURL(getStockData())

    # pshow = Process(target=ShowProcess, args=(SQUEUE,))
    # pshow.start()

    db.close()
    for i in range(CNT):
        processes[i].join()