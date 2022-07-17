#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/180:29
# @File     : WatchListStocksWidget.py
# @Project  : Finance

from PySide2.QtWidgets import QWidget


class WatchListStocksWidget(QWidget):
    """行情 -> 自选股 列表"""

    def __init__(self, parent=None):
        super(WatchListStocksWidget, self).__init__(parent)
