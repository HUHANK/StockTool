#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/8 23:31
# @Author : HuYouLiang
# @File : testMySQL.py
# @Purpose :

import pymysql

db = pymysql.connect(user='root', password='123456', host='localhost', db='financedata')

cursor = db.cursor()
cursor.execute("select * from stock")

while True:
    data = cursor.fetchone()
    if data is None:
        break
    print(data)