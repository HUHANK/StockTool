#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/29 23:44
# @Author : HuYouLiang
# @File : main.py
# @Purpose :
import sys
from PySide2 import QtCore
from common.util import *
from service.TimerService import TimerService

if __name__ == "__main__":
    app = QtCore.QCoreApplication(sys.argv)
    # m = MainP()
    print("main %s\n"%curThreadId())
    mt = TimerService()
    mt.start()

    print("Program start successed!")
    sys.exit(app.exec_())