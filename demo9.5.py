# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-08
Email : weimao@whu.edu.cn
"""
import os
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QAction, QMdiSubWindow


class DeMo:
    count = 0

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo9.5.ui')
        self.ui.menubar.triggered[QAction].connect(self.action)

    def action(self, m):
        if m.text() == 'xinjian':
            sub = QMdiSubWindow()
            self.count += 1
            sub.setWindowTitle('子窗口'+str(self.count))
            self.ui.mdiArea.addSubWindow(sub)
            sub.show()

        if m.text() == 'pingpu':
            self.ui.mdiArea.tileSubWindows()

        if m.text() == 'jilian':
            self.ui.mdiArea.cascadeSubWindows()


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()