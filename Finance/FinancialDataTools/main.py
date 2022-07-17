#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/7/1715:22
# @File     : main.py
# @Project  : Finance

import sys
from PySide2.QtWidgets import QApplication
from FinancialDataTools.ui.MainWindow import MainWindow
from FinancialDataTools.shared.AppConfig import CONFIG


def SystemInit() -> bool:
    pass


if __name__ == "__main__":
    app = QApplication([])
    SystemInit()
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
