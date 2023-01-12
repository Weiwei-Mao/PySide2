# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-08
Email : weimao@whu.edu.cn
"""
import os
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QFont


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo8.5.ui')
        self.ui.pushButton.clicked.connect(self.setfont)
        self.ui.pushButton_2.clicked.connect(self.setcolor)

    def setfont(self):
        from PySide2.QtWidgets import QFontDialog
        (ok, font) = QFontDialog.getFont()
        if ok:
            self.ui.textEdit.setFont(font)

    def setcolor(self):
        from PySide2.QtWidgets import QColorDialog
        color = QColorDialog.getColor()
        self.ui.textEdit.setTextColor(color)


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()