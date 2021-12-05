#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/23 20:33
# @Author : HuYouLiang
# @File : network.py
# @Purpose :

from urllib import request

def wget(url):
    return request.urlopen(url).read().decode("utf8")


