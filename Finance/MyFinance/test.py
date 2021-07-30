#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/8 21:57
# @Author : HuYouLiang
# @File : test.py
# @Purpose :

import cons as ct
import urllib.request
import json

wdate = '20210707'
datepre = ''

symbol = ct._code_to_symbol('600837')
url = ct.DAY_PRICE_URL%(ct.P_TYPE['http'], ct.DOMAINS['ifeng'], ct.K_TYPE['D'], symbol)
print(url)

lines = urllib.request.urlopen(url, timeout=10).read()
#print(lines)

js = json.loads(lines.decode('utf-8'))
print(js)