#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/12 19:16
# @Author : HuYouLiang
# @File : test1.py
# @Purpose :
import os
import shutil



stock_dict = {
'20220102': '1.987',
'20220101': '2.345',
'20220103': '11.234',
'20220104': '0.234',
'20220105': '23.123',
'20220106': '100.00',
}
print(stock_dict)
print(type(stock_dict))

print(min(stock_dict))
print({price : date for date, price in zip(stock_dict.keys(), stock_dict.values())})
t = [(price, date) for date, price in zip(stock_dict.keys(), stock_dict.values())]
print(min(t))

print(sorted(stock_dict.values()))