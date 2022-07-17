#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/1716:11
# @File     : AppConfig.py
# @Project  : Finance

import configparser


class AppConfig(configparser.ConfigParser):
    def __init__(self):
        super(AppConfig, self).__init__()
        self.read("config.ini")
        self.init()

    def init(self):
        self.DB = {}
        self.DB["Host"] = self.get("MySQL", "Host")
        self.DB["Database"] = self.get("MySQL", "Database")
        self.DB["User"] = self.get("MySQL", "User")
        self.DB["Pwd"] = self.get("MySQL", "Password")
        print(self.DB)


CONFIG = AppConfig()
