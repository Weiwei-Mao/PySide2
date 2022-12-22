# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-07
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import image7.img_rc
import time


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo7.3.ui')
        self.ui.menubar.triggered.connect(self.getmenu)
        self.ui.toolBar.actionTriggered.connect(self.getvalue)

        timer = time.localtime(time.time())
        text = '{}年{}月{}日{}时{}分{}秒'.format(timer[0], timer[1], timer[2], timer[3], timer[4], timer[5])
        self.ui.statusbar.showMessage('当前日期时间：' + text)


    def getmenu(self, m):
        from PySide2.QtWidgets import QMessageBox
        QMessageBox.about(self.ui, "提示", "您选择的是："+m.text())

    def getvalue(self, m):
        from PySide2.QtWidgets import QMessageBox
        QMessageBox.about(self.ui, "提示", "您选择的是：" + m.text())


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()