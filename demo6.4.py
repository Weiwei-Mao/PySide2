# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-07
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication, QFileSystemModel
from PySide2.QtUiTools import QUiLoader

## QDirModel准备弃用

class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo6.4.ui')
        self.ui.treeView.setModel(QFileSystemModel())


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()