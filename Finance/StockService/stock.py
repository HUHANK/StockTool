#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/23 21:44
# @Author : HuYouLiang
# @File : stock.py
# @Purpose :

import  json
import pymysql
from common.network import *

shurl = "http://33.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112405339773734141904_1637680512713&pn=1&pz=5000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1637680512714"
szurl = "http://8.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407763465374907266_1637681107141&pn=1&pz=5000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1637681107142"
cyburl = "http://20.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124030638931711443385_1637681363338&pn=1&pz=5000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:80&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1637681363339"

db =pymysql.connect(user='root', password='12345678', host='192.168.2.222', db='FINA')
cursor = db.cursor()

def getStocks(url):
    result = wget(url)
    index1 = result.find('(')+1
    index2 = result.rfind(')')
    js = json.loads(result[index1: index2])

    print(js["data"]["total"])
    for arr in js["data"]["diff"]:
        code = arr["f12"]
        name = arr["f14"]
        MarketCode = arr["f13"]
        sql = "INSERT INTO SEC_CODE(MARKET_CODE, SEC_CODE, " \
            "SEC_NAME) VALUES ('%s', '%s', '%s');"%(
            MarketCode, code, name
        );
        cursor.execute(sql)
    db.commit()

getStocks(shurl)
getStocks(szurl)

