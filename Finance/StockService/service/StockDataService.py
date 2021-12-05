#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 15:38
# @Author : HuYouLiang
# @File : StockDataService.py
# @Purpose :
import sys
sys.path.append("..")
from PySide2 import QtCore

class StockDataService(QtCore.QThread):

    def __init__(self, timer):
        timer.signal_hour.connect(self.slot_UptKlines)

    @QtCore.Slot()
    def slot_UptKlines(self):
        pass