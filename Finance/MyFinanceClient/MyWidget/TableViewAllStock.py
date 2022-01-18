#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/29 21:42
# @Author : HuYouLiang
# @File : TableViewAllStock.py
# @Purpose :

from PySide2.QtWidgets import QTableView, QHeaderView, QAbstractItemView, \
    QDialog, QGraphicsView, QGraphicsScene, QGraphicsPathItem
from PySide2.QtGui import QStandardItemModel, QStandardItem, QPainter, QColor, QPen
from PySide2.QtCore import Qt
from config import GData
from util.comm import *
from DataLayer import *

class GraphicsAxisItem(QGraphicsPathItem):
    def __init__(self, parent = None):
        super(GraphicsAxisItem, self).__init__(parent)


class GraphicsSceneKline(QGraphicsScene):
    def __init__(self, parent = None):
        super(GraphicsSceneKline, self).__init__(parent)
        self.width = 1200;
        self.height = 700;
        self.setSceneRect(-10, -self.height+10, self.width, self.height)
        self.setBackgroundBrush(QColor("#070707"))
        self.showCoordinateSystem()

    def showCoordinateSystem(self):
        pen = QPen(Qt.red, 1)
        len = 10
        self.addLine(0, -len, 0, len, pen)
        self.addLine(-len, 0, len, 0, pen)



class GrphicsViewKline(QGraphicsView):
    def __init__(self, parent = None):
        super(GrphicsViewKline, self).__init__(parent)
        self.setMouseTracking(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHints(QPainter.Antialiasing)

class KlineWidget(QDialog):
    def __init__(self, parent = None):
        super(KlineWidget, self).__init__(parent)
        self.resize(1200, 700)
        self.view = GrphicsViewKline(self)
        self.scene = GraphicsSceneKline(self)
        self.view.setScene(self.scene)



class TableViewAllStock(QTableView):
    def __init__(self, parent=None):
        super(TableViewAllStock, self).__init__(parent)
        # self.mouseDoubleClickEvent()
        self.doubleClicked.connect(self.slotDoubleClicked)
        self.creatUI()
        self.initData()

    def creatUI(self):
        self.model = QStandardItemModel()
        self.setModel(self.model)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.verticalHeader().setDefaultSectionSize(8)
        self.verticalHeader().hide()
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QTableView.NoEditTriggers)
        self.setShowGrid(True)

        arr = ["代码", "名称", "日期", "最新价", "涨跌幅", "涨跌额", "成交量(手)", "成交额", "振幅", "最高", "最低", "今开", "换手率"]
        self.model.setColumnCount(len(arr))
        for i in range(len(arr)):
            self.model.setHeaderData(i, Qt.Horizontal, arr[i])

    def Item(self, var):
        item = QStandardItem(str(var))
        item.setTextAlignment(Qt.AlignVCenter|Qt.AlignHCenter);
        return item

    def initData(self):
        kline = Kline()
        #kline.setYear(2021)
        res = kline.getLatestKlineData()
        for row in res:
            items = []
            items.append(self.Item(row['code']))
            items.append(self.Item(row['SEC_NAME']))
            items.append(self.Item(row['date']))
            items.append(self.Item(row['close']))
            items.append(self.Item(str(row['p_change'])+'%'))
            items.append(self.Item(row['price_change']))
            items.append(self.Item(row['amount']))
            items.append(self.Item(row['turnover']))

            items.append(self.Item(str(row['amplitude'])+'%'))
            items.append(self.Item(row['high']))
            items.append(self.Item(row['low']))
            items.append(self.Item(row['open']))
            items.append(self.Item(str(row['exchange'])+'%'))

            self.model.appendRow(items)

    # QModelIndex index
    def slotDoubleClicked(self, index):
        code = self.model.index(index.row(), 0).data();
        name = self.model.index(index.row(), 1).data();
        d = KlineWidget(self)
        d.setWindowTitle("%s(%s)"%(code, name))
        d.exec()



