# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-05
Email : weimao@whu.edu.cn
"""

from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        self.ui = QUiLoader().load('ui/demo5.11.ui')
        self.ui.pushButton.clicked.connect(self.getvalue)

    def getvalue(self):
        oper = ''
        if self.ui.checkBox.isChecked():
            oper += self.ui.checkBox.text()
        if self.ui.checkBox_2.isChecked():
            oper += '\n' + self.ui.checkBox_2.text()
        if self.ui.checkBox_3.isChecked():
            oper += '\n' + self.ui.checkBox_3.text()
        if self.ui.checkBox_4.isChecked():
            oper += '\n' + self.ui.checkBox_4.text()
        if self.ui.checkBox_5.isChecked():
            oper += '\n' + self.ui.checkBox_5.text()
        from PySide2.QtWidgets import QMessageBox
        QMessageBox.about(self.ui, '提示', '您选择的权限如下：\n'+oper)


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()
