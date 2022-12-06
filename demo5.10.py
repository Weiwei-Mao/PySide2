# -*- coding: utf-8 -*-
"""
Author: Wei Mao
Date  : --
Email : weimao@whu.edu.cn
"""

from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIntValidator
import image.icon_rc   # 在这里导入资源文件


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo5.10.ui')

        self.ui.lineEdit_2.setValidator(QIntValidator(10000000, 99999999))
        self.ui.pushButton_1.clicked.connect(self.login)
        self.ui.radioButton.toggled.connect(self.select)

    def login(self):
        from PySide2.QtWidgets import QMessageBox

        info1 = self.ui.lineEdit_1.text()
        info2 = self.ui.lineEdit_2.text()
        QMessageBox.about(self.ui, '登录信息',
                          '用户名：' + info1 + '密码：' + info2)

    def select(self):
        if self.ui.radioButton.isChecked():
            QMessageBox.about(self.ui, '提示', '您选择的是  管理员  登录')
        if self.ui.radioButton_2.isChecked():
            QMessageBox.about(self.ui, '提示', '您选择的是  普通用户  登录')


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()
