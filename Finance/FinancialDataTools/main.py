#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/1715:22
# @File     : main.py
# @Project  : Finance

import os
import sys

# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide2.QtWidgets import QApplication

from FinancialDataTools.shared.AppConfig import CONFIG
from FinancialDataTools.ui.MainWindow import MainWindow


def SystemInit() -> bool:
    pass


if __name__ == "__main__":
    app = QApplication([])
    SystemInit()
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
