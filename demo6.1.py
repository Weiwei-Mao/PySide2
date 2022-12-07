# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-06
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QBasicTimer


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo6.1.ui')
        self.timer = QBasicTimer()
        self.ui.pushButton.clicked.connect(self.running)

    def running(self):
        if self.timer.isActive():
            self.timer.stop()
            self.ui.pushButton.setText("开始")
            self.ui.progressBar.setMaximum(100)
            self.ui.progressBar_2.setMaximum(100)
            self.ui.progressBar_3.setMaximum(100)
            self.ui.progressBar_4.setMaximum(100)
        else:
            self.timer.start(100, self.ui)
            self.ui.pushButton.setText("结束")
            self.ui.progressBar.setMinimum(0)
            self.ui.progressBar.setMaximum(0)
            self.ui.progressBar_2.setMinimum(0)
            self.ui.progressBar_2.setMaximum(0)
            self.ui.progressBar_3.setMinimum(0)
            self.ui.progressBar_3.setMaximum(0)
            self.ui.progressBar_4.setMinimum(0)
            self.ui.progressBar_4.setMaximum(0)


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()