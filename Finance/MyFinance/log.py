#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 16:18
# @Author : HuYouLiang
# @File : log.py
# @Purpose :

import logging
from logging import handlers
from config import *
from util import *


class CLog(object):
    level_relations={
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }#日志级别关系映射

    def __init__(self):
        mkdir(LOG_DIR)
        logFile = LOG_DIR + "log.txt"
        self.logger = logging.getLogger(logFile)
        formatStr = logging.Formatter(LOG_FORMAT)
        self.logger.setLevel(self.level_relations.get(LOG_LEVEL.lower()))
        sh = logging.StreamHandler()
        sh.setFormatter(formatStr)
        th = handlers.TimedRotatingFileHandler(filename=logFile, when='D', backupCount=15, encoding='utf-8')
        th.setFormatter(formatStr)
        self.logger.addHandler(th)
        self.logger.addHandler(sh)

    def Debug(self, msg):
        self.logger.debug(msg)
    def Info(self, msg):
        self.logger.info(msg)
    def Warning(self, msg):
        self.logger.warning(msg)
    def Error(self, msg):
        self.logger.error(msg)

# if __name__ == "__main__":
#     log = CLog()
#     log.Error("debug")


