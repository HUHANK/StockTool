#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/1 18:40
# @Author : HuYouLiang
# @File : DataLayer.py
# @Purpose :

from config import GData
from util.comm import *

#Kline数据的处理
class Kline:
    def __init__(self):
        self.db = GData['db']
        self.year = GetNowYear()

    def setYear(self, year):
        self.year = year

    def tableName(self):
        return "kline_%s"%(self.year)

    def getMaxDate(self):
        sql = "SELECT max(date) date FROM %s"%(self.tableName())
        ret = self.db.select(sql)
        if len(ret) > 0:
            return ret[0]['date']

    def getLatestKlineData(self):
        sql = "SELECT a.SEC_NAME, b.* FROM sec_code a, %s b where a.SEC_CODE=b.`code` AND date = '%s'"%(
            self.tableName(),  self.getMaxDate()
        )
        ret = self.db.select(sql)
        return ret


