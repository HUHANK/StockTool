#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/1821:32
# @File     : MThread.py
# @Project  : Finance

from PySide2.QtCore import QThread


class MQEventLoopThread(QThread):
    """Qt线程 事件循环执行方式"""

    def __init__(self, parent=None):
        super(MQEventLoopThread, self).__init__(parent)
        self.moveToThread(self)

    def run(self) -> None:
        print("MQEventLoopThread started...")
        self.exec_()
