# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-06
Email : weimao@whu.edu.cn
"""

from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo5.12.ui')

        lst = ['总经理', '副总经理', '人事部经理', '财务部经理', '部门经理', '普通员工']
        self.ui.comboBox.addItems(lst)
        self.ui.comboBox.currentIndexChanged.connect(self.showinfo)

    def showinfo(self):
        self.ui.label_2.setText('您选择的职位是：' + self.ui.comboBox.currentText())


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()