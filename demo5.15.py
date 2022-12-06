# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-06
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo5.15.ui')
        self.ui.pushButton.clicked.connect(self.addtab)
        self.ui.pushButton_2.clicked.connect(self.deltab)
        self.ui.tabWidget.currentChanged.connect(self.gettab)

    def addtab(self):
        self.ui.atab = QWidget()
        name = 'tab_' + str(self.ui.tabWidget.count() + 1)
        self.ui.atab.setObjectName(name)
        self.ui.tabWidget.addTab(self.ui.atab, name)

    def deltab(self):
        self.ui.tabWidget.removeTab(self.ui.tabWidget.currentIndex())

    def gettab(self, currentIndex):
        from PySide2.QtWidgets import QMessageBox
        QMessageBox.about(self.ui, '提示',
                          '您选择了' + self.ui.tabWidget.tabText(currentIndex) + '选项卡，索引为：' + str(
                              self.ui.tabWidget.currentIndex()))


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()