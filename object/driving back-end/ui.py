# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import  sys
import os
from PyQt4 import QtCore, QtGui
from function import *
from page import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
class Main_ui(QtGui.QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("平安驾校数据库管理系统")
        self.setGeometry(QtCore.QRect(200, 200, 1121, 831))
        self.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = Find_change()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = Add()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = Re()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.addTab(self.tab_3, _fromUtf8(""))
        self.setTabText(self.indexOf(self.tab_1), _translate("Dialog", "查询与修改", None))
        self.setTabText(self.indexOf(self.tab_2), _translate("Dialog", "添加用户", None))
        self.setTabText(self.indexOf(self.tab_3), _translate("Dialog", "删除用户", None))

app = QtGui.QApplication(sys.argv)
qb = Main_ui()

qb.show()

sys.exit(app.exec_())