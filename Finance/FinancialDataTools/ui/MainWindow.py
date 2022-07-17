#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/1715:38
# @File     : MainWindow.py
# @Project  : Finance

from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, \
    QTabWidget, QStatusBar

from FinancialDataTools.ui.quotes.AllMarketStocksWidget import AllMarketStocksWidget
from FinancialDataTools.ui.quotes.WatchListStocksWidget import WatchListStocksWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(1400, 800)
        # centralWidget
        self.setCentralWidget(QWidget(self))
        self.centralWidget().setObjectName("centralWidget")

        # Statusbar
        self.setStatusBar(QStatusBar(self))
        self.statusBar().setObjectName("statusBar")

        # tabWidget
        self.tabWidget = MainWindowTab(self.centralWidget())

        layout = QVBoxLayout(self.centralWidget())
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.tabWidget)


class MainWindowTab(QTabWidget):
    def __init__(self, parent=None):
        super(MainWindowTab, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # 沪深京
        self.addTab(AllMarketStocksWidget(self), u"沪深京")
        # 自选股
        self.addTab(WatchListStocksWidget(self), u"自选股")

        self.setCurrentIndex(0)
