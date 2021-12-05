#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 16:15
# @Author : HuYouLiang
# @File : util.py
# @Purpose :

import time, threading, os
from urllib import request
import datetime

def getCurrentDate():
    return time.strftime("%Y%m%d", time.localtime())

def getCurrentTime():
    return time.strftime("%H%M%S", time.localtime())

#获取当前日期的前几天或后几天的日期
def getNowIntervalDate(interval):
    now = datetime.date.today()
    ret = now
    if (interval < 0):
        ret = now - datetime.timedelta(days=-interval)
    else:
        ret = now + datetime.timedelta(days=interval)
    return ret.strftime("%Y%m%d")

def curThreadId():
    return threading.currentThread().ident

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    if not os.path.exists(path):
        os.makedirs(path)

def wget(url):
    return request.urlopen(url).read().decode("utf8")