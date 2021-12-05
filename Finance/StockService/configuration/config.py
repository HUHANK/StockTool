#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/28 21:08
# @Author : HuYouLiang
# @File : config.py
# @Purpose : 全局配置参数

#数据库配置
MYSQL_HOST = "192.168.2.222"
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PWD  = '12345678'
MYSQL_DB   = 'FINA'

# 日志配置
LOG_DIR = "./log/"
LOG_FORMAT = "%(asctime)s|%(pathname)s[line:%(lineno)d]|(%(process)d/%(thread)d)|%(levelname)s: %(message)s"
LOG_LEVEL = "debug"
