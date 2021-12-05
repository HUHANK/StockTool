#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 16:19
# @Author : HuYouLiang
# @File : main.py
# @Purpose :
import  time, traceback
import  log
from util import *
from StockProcess import  StockInexes, StockCode, StockKline

currentDate = ""

def MainProcess():
    global currentDate
    if currentDate != getCurrentDate():
        currentDate = getCurrentDate()
        p = StockInexes()
        p.start()
        p = StockCode()
        p.start()
        p = StockKline()
        p.start()

if __name__ == "__main__":
    Log = log.CLog()
    Log.Info("MyFinance程序启动...")
    while True:
        try:
            MainProcess()
        except:
            print(traceback.format_exc())
        time.sleep(0.1)
