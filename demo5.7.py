# -*- coding: utf-8 -*-
"""
Author: Wei Mao
Date  : --
Email : weimao@whu.edu.cn
"""

from PySide2.QtWidgets import QApplication, QLineEdit
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIntValidator


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/demo5.7.ui')

        self.ui.lineEdit_2.setValidator(QIntValidator(10000000, 99999999))
        self.ui.pushButton_1.clicked.connect(self.login)

    def login(self):
        from PySide2.QtWidgets import QMessageBox

        info1 = self.ui.lineEdit_1.text()
        info2 = self.ui.lineEdit_2.text()
        QMessageBox.about(self.ui, '登录信息',
                          '用户名：' + info1 + '密码：' + info2)


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()
