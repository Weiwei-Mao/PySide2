# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-07
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QFont


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo6.9.ui')
        self.ui.dial.valueChanged.connect(self.setfontsize)

    def setfontsize(self):
        value = self.ui.dial.value()
        self.ui.label.setFont(QFont('楷体', value))


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()