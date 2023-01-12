# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-08
Email : weimao@whu.edu.cn
"""
import os
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QInputDialog
from PySide2.QtWidgets import QLineEdit


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo8.4.ui')
        self.ui.lineEdit.returnPressed.connect(self.getname)
        self.ui.lineEdit_2.returnPressed.connect(self.getage)
        self.ui.lineEdit_3.returnPressed.connect(self.getgrade)
        self.ui.lineEdit_4.returnPressed.connect(self.getscore)

    def getname(self):
        name, ok = QInputDialog.getText(self.ui, "姓名", "请输入姓名", QLineEdit.Normal, "明日科技")
        if ok:
            self.ui.lineEdit.setText(name)

    def getage(self):
        age, ok = QInputDialog.getInt(self.ui, "年龄", "请输入年龄", 20, 1, 100, 1)
        if ok:
            self.ui.lineEdit_2.setText(str(age))

    def getgrade(self):
        grade, ok = QInputDialog.getItem(self.ui, "班级", "请选择班级", ('三年一班', '三年二班', '三年三班'), 0, False)
        if ok:
            self.ui.lineEdit_3.setText(grade)

    def getscore(self):
        score, ok = QInputDialog.getDouble(self.ui, "分数", "请选择分数", 0.01, 0, 100, 2)
        if ok:
            self.ui.lineEdit.setText(score)


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()