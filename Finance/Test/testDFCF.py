#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/15 21:42
# @Author : HuYouLiang
# @File : testDFCF.py
# @Purpose :

from urllib import request
import  json
import re
import pandas as pd
import pymysql
import os

def getHtml(url):
    html = request.urlopen(url).read()
    html = html.decode('utf8')
    #print(html)
    return html

def WriteFile(path,msg):
    #with open('test.txt', 'w') as f:
   # f.write('Hello, world!')
    file = open(path, 'a',encoding='gbk', errors='ignore')
    f = file.write(str(msg.decode('utf-8')))
    file.close()

# 获取K线数据
url1 = "http://65.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery112406979084319890396_1636986931189&secid=0.300691&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=0&end=20500101&lmt=240&_=1636986931206"
url = "http://18.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112404826355556865607_1636986272476&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1636986272477"
html = getHtml(url)
index1 = html.find('(')+1;
index2 = html.rfind(')');

print(html[index1:index2])
js = json.loads(html[index1:index2])
print(js["data"])
print(json.dumps(js, sort_keys=False, indent=2))
