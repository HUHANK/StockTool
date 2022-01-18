#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/29 22:31
# @Author : HuYouLiang
# @File : TestQtThread.py
# @Purpose :
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QThread
import  sys, threading

class MyQtThread(QThread):
    def __init__(self):
        super(MyQtThread, self).__init__()

    def run(self):
        print(threading.currentThread().ident)

if __name__ == "__main__":
    app = QApplication([])
    t = MyQtThread()
    t.start()
    print(threading.currentThread().ident)
    sys.exit(app.exec_())















