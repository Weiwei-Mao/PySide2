# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-08
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo8.2.ui')
        self.ui.pushButton.clicked.connect(self.bindlist)

    def bindlist(self):
        from PySide2.QtWidgets import QFileDialog
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.ExistingFiles)
        dir.setDirectory('C:\\')
        dir.setNameFilter('图片文件(*.jpg *.png *.bmp *.ico *.gif)')
        if dir.exec_():
            self.ui.listWidget.addItems(dir.selectedFiles())


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()