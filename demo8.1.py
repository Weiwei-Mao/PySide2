# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-08
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMessageBox


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo8.1.ui')
        self.ui.pushButton.clicked.connect(self.info)
        self.ui.pushButton_2.clicked.connect(self.warn)
        self.ui.pushButton_3.clicked.connect(self.question)
        self.ui.pushButton_4.clicked.connect(self.critical)
        self.ui.pushButton_5.clicked.connect(self.about)

    def info(self):
        select = QMessageBox.information(self.ui, '消息', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No)
        if select == QMessageBox.Yes:
            QMessageBox.information(self.ui, '提醒', '您同意了本次请求...')

    def warn(self):
        QMessageBox.warning(self.ui, '警告', '这是一个警告对话框')

    def question(self):
        QMessageBox.question(self.ui, '问答', '这是一个问答对话框')

    def critical(self):
        QMessageBox.critical(self.ui, '错误', '这是一个错误对话框')

    def about(self):
        QMessageBox.about(self.ui, '关于', '这是一个关于对话框')


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()