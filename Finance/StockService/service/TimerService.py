#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 13:05
# @Author : HuYouLiang
# @File : TimerService.py
# @Purpose :
import sys
sys.path.append("..")
from PySide2 import QtCore
from common import util

class TimerService (QtCore.QThread):
    signal_day = QtCore.Signal()
    signal_hour = QtCore.Signal()

    def __init__(self):
        super(TimerService, self).__init__()
        self.moveToThread(self)
        self._timer = None
        self._interval = 1000
        self._curDate = ""

    @QtCore.Slot()
    def slot_timeout(self):
        if self._curDate != util.getCurrentDate():
            self._curDate = util.getCurrentDate()
            self.signal_day.emit()

    def run(self):
        self._timer = QtCore.QTimer()
        self._timer.setInterval(self._interval)
        self._timer.timeout.connect(self.slot_timeout)
        self._timer.start()
        self.exec_()