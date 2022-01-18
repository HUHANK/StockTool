#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/30 21:59
# @Author : HuYouLiang
# @File : comm.py
# @Purpose :

import time

#'20211230'
def GetNowDate():
    t = time.localtime(time.time())
    ret = (t.tm_year*100 + t.tm_mon)*100 + t.tm_mday;
    return "%s"%(ret)

def GetNowYear():
    t = time.localtime(time.time())
    return t.tm_year;

