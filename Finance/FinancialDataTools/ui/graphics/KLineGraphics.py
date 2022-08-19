#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Hank
# @Time     : 2022/8/1922:54
# @File     : KLineGraphics.py
# @Project  : Finance

from PySide2.QtWidgets import QGraphicsView, QGraphicsScene,QGraphicsItem, \
    QGraphicsPathItem

class KLineView(QGraphicsView):
    def __init__(self, parent=None):
        super(KLineView, self).__init__(parent)

class KLineScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(KLineScene, self).__init__(parent)
