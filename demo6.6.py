# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-07
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import image.logo_rc


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo6.6.ui')
        self.ui.treeWidget.clicked.connect(self.gettreetxt)

    def gettreetxt(self):
        item = self.ui.treeWidget.currentItem()
        from PySide2.QtWidgets import QMessageBox
        QMessageBox.about(self.ui, '提示', '您选择的是：%s -- %s'%(item.text(0), item.text(1)))


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()