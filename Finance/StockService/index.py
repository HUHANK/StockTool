#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/23 22:45
# @Author : HuYouLiang
# @File : index.py
# @Purpose :
import  json
import pymysql
from common.network import *

url1 = "http://79.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112401400107453569246_1637678610637&pn=1&pz=2000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+s:2&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152&_=1637678610638"
url2 = "http://23.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124044518063086011184_1637679493333&pn=1&pz=2000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:5&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152&_=1637679493334"

db =pymysql.connect(user='root', password='12345678', host='192.168.2.222', db='FINA')
cursor = db.cursor()

def getStockIndexes(url):
    result = wget(url)
    index1 = result.find('(')+1;
    index2 = result.rfind(')');
    js = json.loads(result[index1: index2])
    #print(json.dumps(js, sort_keys=False, indent=2))

    #print(len(js["data"]["diff"]));

    for arr in js["data"]["diff"]:
        code = arr["f12"]
        name = arr["f14"]
        sql = ""
        marketCode = arr["f13"]

        sql = "INSERT INTO SEC_INDEX(MARKET_CODE, SEC_CODE," \
              "SEC_NAME) VALUES ('%s', '%s', '%s');"%(
            marketCode, code, name
        )
        print(sql)
        cursor.execute(sql)
    db.commit()

getStockIndexes(url1)
getStockIndexes(url2)