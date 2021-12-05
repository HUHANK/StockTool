#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/30 23:20
# @Author : HuYouLiang
# @File : util.py
# @Purpose :
import time, threading

def getCurrentDate():
    return time.strftime("%Y%m%d", time.localtime())

def getCurrentTime():
    return time.strftime("%H%M%S", time.localtime())

def curThreadId():
    return threading.currentThread().ident










