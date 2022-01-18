#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 22:21
# @Author : HuYouLiang
# @File : main.py
# @Purpose :

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from MyWidget.MainWindowTabWidget import MainWinowTabWidget
from config import *
from util.DBMySQL import  CMySQL


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Finance")
        self.resize(1000, 600)
        #self.setStyleSheet("background-color:yellow")
        self.CreateUI()

    def CreateUI(self):
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.mainTab = MainWinowTabWidget(self.centralwidget)
        layout = QVBoxLayout()
        layout.addWidget(self.mainTab)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget.setLayout(layout)


if __name__ == "__main__":
    GData['db'] = CMySQL()
    GData['db'].connect()
    app = QApplication([])
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())