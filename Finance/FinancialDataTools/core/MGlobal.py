#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/1822:29
# @File     : MGlobal.py
# @Project  : Finance

from PySide2.QtCore import QObject, Slot, Signal
from FinancialDataTools.dao.MySQLService import MySQLService

class MGlobal(QObject):
    def __init__(self, parent=None):
        super(MGlobal, self).__init__(parent)
        self.dbservice = None

    def init(self):
        self.dbservice = MySQLService()
        self.dbservice.start()

        self.sigqueryAllMarketStocks.connect(self.dbservice.queryAllMarketStocks)

    # SIGNAL
    sigqueryAllMarketStocks=Signal()



gGlobal=MGlobal()