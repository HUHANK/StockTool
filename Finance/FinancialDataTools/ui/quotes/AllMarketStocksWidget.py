#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/1723:51
# @File     : AllMarketStocksWidget.py
# @Project  : Finance

from PySide2.QtWidgets import QWidget, QTableView, QHBoxLayout, QHeaderView, QAbstractItemView
from PySide2.QtGui import  QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt, Slot, Signal
from FinancialDataTools.core.MGlobal import gGlobal

class AllMarketStocksWidget(QWidget):
    """
    # 沪深京股票列表空间
    """
    def __init__(self, parent=None):
        super(AllMarketStocksWidget, self).__init__(parent)
        self.initUI()
        gGlobal.sigqueryAllMarketStocks.emit()

    def initUI(self):
        self.table = AllMarketStocksTableView(self)
        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.table)


class AllMarketStocksTableView(QTableView):
    def __init__(self, parent=None):
        super(AllMarketStocksTableView, self).__init__(parent)
        self.initUI()
        gGlobal.dbservice.sigqueryAllMarketStocksRet[dict].connect(self.addOneRow)

    def initUI(self):
        self.model = QStandardItemModel()
        self.setModel(self.model)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.verticalHeader().setDefaultSectionSize(8)
        self.verticalHeader().hide()
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QTableView.NoEditTriggers)
        self.setShowGrid(True)
        self.initUI_Header()

    def initUI_Header(self):
        arr = [u"证券代码", u"证券名称", u"日期", u"开盘价", u"最高价", u"最低价", u"收盘价", u"前收盘价", u"成交量(股)", u"成交额(元)",
               u"换手率", u"涨跌幅", u"上市日期", u"所属行业", u"所属行业类别"]
        self.model.setColumnCount(len(arr))
        for i in range(len(arr)):
            self.model.setHeaderData(i, Qt.Horizontal, arr[i])

    def Item(self, val) -> QStandardItem:
        item = QStandardItem(str(val))
        item.setTextAlignment(Qt.AlignCenter)
        return item

    @Slot(dict)
    def addOneRow(self, row):
        items = []
        items.append(self.Item(row["code"]))
        items.append(self.Item(row["code_name"]))
        items.append(self.Item(row["date"]))
        items.append(self.Item(row["open"]))
        items.append(self.Item(row["high"]))
        items.append(self.Item(row["low"]))
        items.append(self.Item(row["close"]))
        items.append(self.Item(row["preclose"]))
        items.append(self.Item(row["volume"]))
        items.append(self.Item(row["amount"]))
        items.append(self.Item(row["turn"]))
        items.append(self.Item(row["pctChg"]))
        items.append(self.Item(row["ipoDate"]))
        items.append(self.Item(row["industry"]))
        items.append(self.Item(row["industryClassification"]))
        self.model.appendRow(items)

