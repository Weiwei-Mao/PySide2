# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-08
Email : weimao@whu.edu.cn
"""
import os
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo8.3.ui')
        self.ui.pushButton.clicked.connect(self.bindlist)

    def bindlist(self):
        from PySide2.QtWidgets import QFileDialog
        dir = QFileDialog.getExistingDirectory(None, "选择文件夹路径", os.getcwd())
        self.ui.lineEdit.setText(dir)
        lst = os.listdir(dir)
        self.ui.listWidget.addItems(lst)


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()