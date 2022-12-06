# -*- coding:utf-8 -*-
"""
Author：Wei Mao
Date  ：2022-12-06
Email : weimao@whu.edu.cn
"""
from PySide2.QtWidgets import QApplication, QListWidgetItem
from PySide2.QtUiTools import QUiLoader
from collections import OrderedDict


class DeMo:

    def __init__(self):
        # 从文件中加载UI定义

        self.ui = QUiLoader().load('ui/demo5.14.ui')
        dict = OrderedDict({
            '第1名': '战狼2，2017年上映，票房56.83亿',
            '第2名': '哪吒之魔童降世，2019年上映，票房50.12亿',
            '第3名': '流浪地球，2019年上映，票房46.86亿',
            '第4名': '复仇者联盟：终局之战，2019年上映，票房42.50亿',
            '第5名': '红海行动，2018年上映，票房36.51亿',
            '第6名': '唐人街探案2，2018年上映，票房33.98亿',
            '第7名': '美人鱼，2016年上映，票房33.86亿',
            '第8名': '我和我的祖国，2019年上映，票房31.71亿',
            '第9名': '我不是药神，2018年上映，票房31.00亿',
            '第10名': '中国机长，2019年上映，票房29.13亿'
        })

        for key, value in dict.items():
            self.ui.item = QListWidgetItem(self.ui.listWidget)
            self.ui.item.setText(key + ':' + value)
            self.ui.item.setToolTip(value)
        self.ui.listWidget.itemClicked.connect(self.gettext)

    def gettext(self, item):
        if item.isSelected():
            from PySide2.QtWidgets import QMessageBox
            QMessageBox.about(self.ui, '提示', '您选择的是：'+item.text())


app = QApplication([])
stats = DeMo()
stats.ui.show()
app.exec_()
app.exec_()