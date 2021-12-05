#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/4 20:32
# @Author : HuYouLiang
# @File : TestQt.py
# @Purpose :

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import PySide2.QtCore

def handleclick():
    print("button is clicked")
    QMessageBox.information(window, "hint", "button is clicked", QMessageBox.Ok)

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300,310)
window.setWindowTitle("Test Qt")

button = QPushButton(window)
button.resize(80,20)
button.setText("Test Button")
button.clicked.connect(handleclick)


window.show()
app.exec_()