# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-06
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QDate


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo5.17.ui')
        self.ui.calendarWidget.selectionChanged.connect(self.getdate)

    def getdate(self):
        from PySide2.QtWidgets import QMessageBox
        date = QDate(self.ui.calendarWidget.selectedDate())
        year = date.year()
        month = date.month()
        day = date.day()
        QMessageBox.about(self.ui, '提示', str(year)+'-'+str(month)+'-'+str(day))


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()