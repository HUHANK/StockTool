#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/1821:44
# @File     : MySQLService.py
# @Project  : Finance

from FinancialDataTools.shared.MThread import MQEventLoopThread
from FinancialDataTools.shared.MySQL import MySQL
from FinancialDataTools.shared.AppConfig import CONFIG

from PySide2.QtCore import  QObject, Signal, Slot

class MySQLService(MQEventLoopThread):
    """"""
    # SIGNAL
    sigqueryAllMarketStocksRet = Signal(dict)

    def __init__(self):
        super(MySQLService, self).__init__()
        self.mysql = None

    def run(self) -> None:
        self.mysql = MySQL(CONFIG.DB["Host"], CONFIG.DB["Database"],
                           CONFIG.DB["User"], CONFIG.DB["Pwd"], CONFIG.DB["Port"])
        print("MySQLService started!")
        self.exec_()

    @Slot()
    def queryAllMarketStocks(self):
        sql = "SELECT sb.code , sb.code_name , sb.ipoDate , sb.outDate , sb.`type` , sb.status , si.industry , si.industryClassification , \
            kd.`date`, kd.`open` , kd.high , kd.low , kd.`close` , kd.preclose , kd.volume , kd.amount , kd.turn , kd.tradestatus , \
            kd.pctChg , kd.peTTM , kd.psTTM , kd.pcfNcfTTM , kd.pbMRQ  \
            FROM stock_basic sb  LEFT JOIN stock_industry si on sb.code = si.code \
            LEFT JOIN k_d_2022 kd on sb.code = kd.code  \
            WHERE sb.`type` = '1' AND  kd.`date`  = (SELECT max(`date`) from k_d_2022) and kd.adjustflag = '1'  \
            LIMIT 0, 10"
        ret = self.mysql.select(sql)
        for row in ret:
            print(row)
            self.sigqueryAllMarketStocksRet[dict].emit(row)
