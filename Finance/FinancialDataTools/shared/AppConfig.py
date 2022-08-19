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
        self.DB = {"Host": self.get("MySQL", "Host"), "Database": self.get("MySQL", "Database"),
                   "User": self.get("MySQL", "User"), "Pwd": self.get("MySQL", "Password")}
        self.DB["Port"] = int(self.get("MySQL", "Port"))
        print(self.DB)


CONFIG = AppConfig()
