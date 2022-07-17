#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/1723:51
# @File     : AllMarketStocksWidget.py
# @Project  : Finance

from PySide2.QtWidgets import QWidget


class AllMarketStocksWidget(QWidget):
    """
    # 沪深京股票列表空间
    """
    def __init__(self, parent=None):
        super(AllMarketStocksWidget, self).__init__(parent)
