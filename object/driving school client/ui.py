# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
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
    def __init__(self):
        super().__init__()
        self.setGeometry(QtCore.QRect(200, 200, 1121, 831))
        self.setObjectName(_fromUtf8("tabWidget"))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.label = QtGui.QLabel(self.tab_6)
        self.label.setGeometry(QtCore.QRect(210, 0, 551, 801))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setFont(QtGui.QFont("Timers" ,12))
        self.graphicsView = QtGui.QGraphicsView(self.tab_6)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 211, 581))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.calendarWidget = QtGui.QCalendarWidget(self.tab_6)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 580, 211, 221))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.tab_6)
        self.graphicsView_2.setGeometry(QtCore.QRect(770, 0, 391, 831))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label_2 = QtGui.QLabel(self.tab_6)
        self.label_2.setGeometry(QtCore.QRect(1, 4, 211, 571))
        self.label_2.setText(_fromUtf8(""))
        png = QtGui.QPixmap(_fromUtf8("G:/驾校管理系统客户端/picture/3.jpg")).scaled(self.label_2.width(), self.label_2.height())
        self.label_2.setPixmap(png)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_6)
        self.label_3.setGeometry(QtCore.QRect(771, 4, 341, 801))
        self.label_3.setText(_fromUtf8("ewfwafeaf"))
        png = QtGui.QPixmap(_fromUtf8("G:/驾校管理系统客户端/picture/2.jpg")).scaled(self.label_3.width(),self.label_3.height())
        self.label_3.setPixmap(png)

        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.addTab(self.tab_6, _fromUtf8(""))
        self.tab_5 = Apply(cl)
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.addTab(self.tab_5, _fromUtf8(""))
        self.tab_3 = download_video(cl,cl.get_video())
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = Appointment(cl,cl.all_teacher())
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.addTab(self.tab_4, _fromUtf8(""))
        self.tab = test(cl)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi()
        self.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "平安驾校客户端", None))
        self.setWindowIcon(QtGui.QIcon("icon/sign.jpg"))
        self.label.setStyleSheet("background-image:url(picture/4.jpg)")
        self.label.setText(_translate("Dialog", "信息", None))
        self.setTabText(self.indexOf(self.tab_6), _translate("Dialog", "个人信息", None))
        self.setTabText(self.indexOf(self.tab_5), _translate("Dialog", "报名", None))
        self.setTabText(self.indexOf(self.tab_3), _translate("Dialog", "教学视频下载", None))
        self.setTabText(self.indexOf(self.tab_4), _translate("Dialog", "练车预约", None))
        self.setTabText(self.indexOf(self.tab), _translate("Dialog", "科一测试", None))






#注册
class Ui_Sign_in(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName(_fromUtf8("注册"))
        self.resize(400, 300)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/sign_in.png')))  # 设置背景图片
        self.setPalette(palette1)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 100, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(100, 130, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(170, 40, 51, 21))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(_fromUtf8("font: 11pt \"宋体\""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(170, 100, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 130, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 160, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "注册", None))
        self.pushButton.setText(_translate("self", "注册", None))
        self.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.sign_in)
        self.label.setText(_translate("self", "用户名", None))
        self.label_2.setText(_translate("self", "  密码", None))
        self.label_3.setText(_translate("self", "再输一次密码", None))
        self.label_4.setText(_translate("self", " 注册", None))
        self.setWindowIcon(QtGui.QIcon("icon/sign.jpg"))
    def sign_in(self):
        if self.lineEdit_2.text() != self.lineEdit_3.text():
            reply = QtGui.QMessageBox.question(self, '两次密码不一致错误', "修改信息？", "确定")
        else:
            data = cl.sign_in({'user':self.lineEdit.text(),'password':self.lineEdit_2.text()})
            print(data)
            if data == "用户已经存在":
                reply = QtGui.QMessageBox.question(self, '注册失败', "用户已存在", "确定")
            else:
                reply = QtGui.QMessageBox.question(self, '注册成功', "欢迎使用平安驾校网络系统","确定")
                self.close()

#登入
class Enter(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        palette1 = QtGui.QPalette()
        self.setWindowTitle("平安驾校")
        self.resize(400, 300)
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/enter.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(90, 200, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 200, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
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
        self.setWindowIcon(QtGui.QIcon("icon/sign.jpg"))
        self.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.ui_enter)
        self.pushButton_2.setText(_translate("self", "注册", None))
        self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.ui_login)
        self.label.setText(_translate("self", "  账号", None))
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_2.setText(_translate("self", "  密码", None))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_3.setText(_translate("self", "  欢迎登入", None))
    def ui_enter(self):
        data = cl.enter(self.lineEdit.text(),self.lineEdit_2.text())
        if data  == "account_error" :
            reply = QtGui.QMessageBox.question(self, '账号或密码错误', "放弃登入？", QtGui.QMessageBox.Yes,
                                               QtGui.QMessageBox.No)
            # 调用提示窗口方法question，第一个参数为标题，第二个为问题文本，后面是选项
            if reply == QtGui.QMessageBox.Yes:
                self.close()
        else:
            self.Main_ui = Main_ui()
            vis_text = f"用户名：{cl.account.look_account()['user']}\n账号创立时间:{cl.account.look_account()['time']}\n身份:{cl.account.look_account()['identity']}\n"
            if   cl.account.identity  ==  "visitor":
                cl.img_synchronization()
                self.Main_ui.label.setText(vis_text)
            else:
                cl.img_synchronization()
                stu_text = f"ID:{cl.account.look_account()['user']}\n名字：{cl.account.look_account()['name']}\n出生日期：{cl.account.look_account()['life']}\n地址：{cl.account.look_account()['address']}\n电话：{cl.account.look_account()['phone']}\n"
                self.Main_ui.label.setText(vis_text+stu_text)
            self.Main_ui.show()
            self.close()
            print("退出")
    def ui_login(self):
        self.sign_in = Ui_Sign_in()
        self.sign_in.show()







app = QtGui.QApplication(sys.argv)
qb = Enter()

qb.show()

sys.exit(app.exec_())



