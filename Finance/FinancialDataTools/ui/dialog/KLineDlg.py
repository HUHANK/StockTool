#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/8/1922:43
# @File     : KLineDlg.py
# @Project  : Finance

from PySide2.QtWidgets import QDialog


class KLineDlg(QDialog):
    """
    # 显示股票K线的对话框
    """
    def __init__(self, code, parent=None):
        super(KLineDlg, self).__init__(parent)
        self.code = code
        self.initUI()


    def initUI(self):
        self.resize(800, 500)
        self.setWindowTitle(self.code)
