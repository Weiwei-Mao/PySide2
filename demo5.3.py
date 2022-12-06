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
        # 5.3到5.6均可以采用该文件打开
        self.ui = QUiLoader().load('ui/demo5.6.ui')


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()
