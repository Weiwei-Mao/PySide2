# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-07
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import image7.img_rc


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo7.1.ui')
        self.ui.menubar.triggered.connect(self.getmenu)

    def getmenu(self, m):
        from PySide2.QtWidgets import QMessageBox
        QMessageBox.about(self.ui, "提示", "您选择的是："+m.text())


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()