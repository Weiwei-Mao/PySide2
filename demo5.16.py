# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-06
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import image.icon16_rc


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo5.16.ui')


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()