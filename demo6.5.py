# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-07
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QStandardItemModel, QStandardItem


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo6.4.ui')
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['年级', '班级', '姓名', '分数'])

        name = ['马云', '马化腾', '李彦宏', '王兴', '刘强东', '董明珠', '张一鸣', '任正非', '丁磊', '程维']
        score = [65, 89, 45, 68, 90, 100, 99, 76, 85, 73]

        import random
        for i in range(0, 6):
            grade = QStandardItem('%s年级' % (i + 1))
            model.appendRow(grade)
            for j in range(0, 4):
                itemClass = QStandardItem('%s班' % (j+1))
                itemName = QStandardItem(name[random.randrange(10)])
                itemScore = QStandardItem(str(score[random.randrange(10)]))
                grade.appendRow([QStandardItem(''), itemClass, itemName, itemScore])
        self.ui.treeView.setModel(model)


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()