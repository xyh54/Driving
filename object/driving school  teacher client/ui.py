import  sys
import os
from PyQt4 import QtCore, QtGui
from function import client
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
cl = client()
class Main_ui(QtGui.QTabWidget):
    def __init__(self,account):
        super().__init__()
        self.setGeometry(QtCore.QRect(200, 200, 1121, 831))
        self.setObjectName(_fromUtf8("tabWidget"))
        self.tab = Show_inf(account)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.addTab(self.tab,_fromUtf8(""))
        self.tab2 = Uploading(cl)
        self.addTab(self.tab2, _fromUtf8(""))
        self.tab3 = Appointment(account)
        self.addTab(self.tab3,_fromUtf8(""))
        self.tab4 = Cat_stu(cl)
        self.addTab(self.tab4, _fromUtf8(""))
        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "平安驾校老师端", None))
        self.setTabText(self.indexOf(self.tab), _translate("Dialog", "老师信息", None))
        self.setTabText(self.indexOf(self.tab2), _translate("Dialog", "视频上传", None))
        self.setTabText(self.indexOf(self.tab3), _translate("Dialog", "预约信息", None))
        self.setTabText(self.indexOf(self.tab4), _translate("Dialog", "学号查学生", None))
        self.setWindowIcon(QtGui.QIcon("picture/sign.jpg"))

class Enter(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        palette1 = QtGui.QPalette()
        self.setWindowTitle("平安驾校老师端登入")
        self.resize(400, 300)
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/enter.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        self.setWindowIcon(QtGui.QIcon("picture/sign.jpg"))
        self.setAutoFillBackground(True)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(160, 100, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 130, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 100, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(90, 140, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(160, 40, 91, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.pushButton.setText(_translate("self", "登入", None))
        self.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.ui_enter)
        self.label.setText(_translate("self", "  账号", None))
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_2.setText(_translate("self", "  密码", None))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_3.setText(_translate("self", "  欢迎登入", None))
    def ui_enter(self):
        data = cl.enter(self.lineEdit.text(),self.lineEdit_2.text())
        print(data)
        if data  == "account_error" :
            reply = QtGui.QMessageBox.question(self, '账号或密码错误', "放弃登入？", QtGui.QMessageBox.Yes,
                                               QtGui.QMessageBox.No)
            # 调用提示窗口方法question，第一个参数为标题，第二个为问题文本，后面是选项
            if reply == QtGui.QMessageBox.Yes:
                self.close()
        elif  data[3]  != "teacher":
            reply = QtGui.QMessageBox.question(self, '账号或密码错误', "放弃登入？", QtGui.QMessageBox.Yes,
                                               QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.close()
        else:
            cl.img_synchronization()
            self.Main_ui = Main_ui(data)
            self.Main_ui.show()
            self.close()
            print("退出")








app = QtGui.QApplication(sys.argv)
qb = Enter()

qb.show()

sys.exit(app.exec_())