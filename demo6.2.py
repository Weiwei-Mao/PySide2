# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-07
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QMovie
import image.gif_rc


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo6.2.ui')
        self.ui.pushButton.clicked.connect(self.start_loading)
        self.ui.pushButton_2.clicked.connect(self.stop_loading)

    def start_loading(self):
        self.ui.gif = QMovie('image/loading.gif')
        self.ui.label.setMovie(self.ui.gif)
        self.ui.gif.start()

    def stop_loading(self):
        self.ui.gif.stop()
        # self.ui.label.clear()


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()