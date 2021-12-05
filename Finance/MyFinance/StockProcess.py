#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 16:30
# @Author : HuYouLiang
# @File : StockProcess.py
# @Purpose :
from multiprocessing import Process, Queue
from abc import ABCMeta, abstractmethod
import os
from db import  CMySQL
from util import *
import json

class CProcess:
    __metaclass__ = ABCMeta
    def __init__(self):
        self.process = None

    @abstractmethod
    def run(self):
        print("CProcess PID: %s" % os.getpid())

    def start(self):
        self.process = Process(target=self.run, args=())
        self.process.start()

    def stop(self):
        try:
            if self.process.is_alive():
                self.process.kill()
            self.process.close()
        except ... as e:
            import traceback
            traceback.print_exc()

class StockInexes(CProcess):
    def __init__(self):
        super().__init__()
        self.db = None

    def getData(self, url):
        result = wget(url)
        js = json.loads(result[(result.find('(')+1) : (result.rfind(')'))])
        for arr in js["data"]["diff"]:
            code = arr["f12"]
            name = arr["f14"]
            marketCode = arr["f13"]
            sql = "INSERT INTO SEC_INDEX(MARKET_CODE, SEC_CODE," \
                  "SEC_NAME) VALUES ('%s', '%s', '%s');" % (
                      marketCode, code, name
                  )
            self.db.execUpdate(sql)

    def run(self):
        self.db = CMySQL()
        if (self.db.connect() == False):
            # Log.Error("Database connect error!")
            return

        url1 = "http://79.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112401400107453569246_1637678610637&pn=1&pz=2000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+s:2&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152&_=1637678610638"
        url2 = "http://23.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124044518063086011184_1637679493333&pn=1&pz=2000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:5&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152&_=1637679493334"
        self.getData(url1)
        self.getData(url2)

class StockCode(CProcess):
    def __init__(self):
        super().__init__()
        self.db = None

    def getData(self, url):
        result = wget(url)
        js = json.loads(result[(result.find('(') + 1): (result.rfind(')'))])
        for arr in js["data"]["diff"]:
            code = arr["f12"]
            name = arr["f14"]
            marketCode = arr["f13"]
            sql = "INSERT INTO SEC_CODE(MARKET_CODE, SEC_CODE, " \
                  "SEC_NAME) VALUES ('%s', '%s', '%s');" % (
                      marketCode, code, name
                  )
            self.db.execUpdate(sql)

    def run(self):
        self.db = CMySQL()
        if (self.db.connect() == False):
            # Log.Error("Database connect error!")
            return
        shurl = "http://33.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112405339773734141904_1637680512713&pn=1&pz=5000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1637680512714"
        szurl = "http://8.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407763465374907266_1637681107141&pn=1&pz=5000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1637681107142"
        self.getData(shurl)
        self.getData(szurl)
        
class StockKline(CProcess):
    def __init__(self):
        super(StockKline, self).__init__()
        self.db = None

    def getStockCodes(self):
        sql = "SELECT MARKET_CODE, SEC_CODE FROM sec_code;"
        result = self.db.select(sql)
        return result

    def genUrl(self, arr):
        URL = "http://66.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery112407407881261721598_1637762378256&secid={0}.{1}&ut=" \
              "fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2C" \
              "f58%2Cf59%2Cf60%2Cf61&klt=101&fqt=0&beg={2}&end=20500101&smplmt={3}&lmt=1000000&_=1637762378257"
        surl = URL.format(arr['MARKET_CODE'], arr['SEC_CODE'], getNowIntervalDate(-10), 10)
        print(surl)
        return surl

    def getData(self, url):
        result = wget(url)
        js = json.loads(result[(result.find('(') + 1): (result.rfind(')'))])
        code = js["data"]["code"]
        for line in js["data"]["klines"]:
            arr = line.split(",")
            date = arr[0].replace('-', "")
            tableName = "kline_" + date[0:4]
            # print(date + " -------- " + tableName)
            sql = "INSERT INTO " + tableName + "(";
            sql+= "`code`, `date`, `open`, `high`, `close`, `low`, `amount`, `turnover`, `amplitude`, `p_change`, `price_change`, `exchange`";
            sql+= ") VALUES (" \
                  "'%s',  '%s', %s,   %s,   %s,    %s,   %s,   %s,        %s,         %s,       %s,          %s);"%(
                code, date, arr[1], arr[3], arr[2], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10]
            )
            self.db.execUpdate(sql)

    def run(self):
        self.db = CMySQL()
        if (self.db.connect() == False):
            # Log.Error("Database connect error!")
            return
        result = self.getStockCodes()
        for row in result:
            url = self.genUrl(row)
            self.getData(url)
