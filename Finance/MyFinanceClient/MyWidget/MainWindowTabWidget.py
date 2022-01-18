#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/29 20:58
# @Author : HuYouLiang
# @File : MainWindowTabWidget.py
# @Purpose :
from PySide2.QtWidgets import QTabWidget, QWidget, QVBoxLayout
from MyWidget.TableViewAllStock import  TableViewAllStock

class MainWinowTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(MainWinowTabWidget, self).__init__(parent)
        self.createUI()

    def createUI(self):
        self.tabMain = QWidget()
        self.tabMainTableView = TableViewAllStock(self.tabMain)
        layout = QVBoxLayout()
        layout.addWidget(self.tabMainTableView)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        self.tabMain.setLayout(layout)
        self.addTab(self.tabMain, "主页")

        self.tabOptionalStock = QWidget()
        self.addTab(self.tabOptionalStock, "自选")