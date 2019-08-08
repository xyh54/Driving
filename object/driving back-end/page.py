# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'ui_name.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from function import Function
import time
fu =Function()
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

class amend(QtGui.QWidget):
    def __init__(self,identity,data):
        super().__init__()
        self.data = data
        self.setObjectName(_fromUtf8("self"))
        self.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('img/2.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        self.resize(850, 873)
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 260, 16, 101))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_12 = QtGui.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(40, 90, 72, 15))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(160, 90, 72, 15))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(280, 90, 72, 15))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(390, 90, 72, 15))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(510, 90, 72, 15))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(600, 90, 72, 15))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(730, 90, 72, 15))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(30, 40, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.retranslateUi()
        if identity == "student":
            self.student()
        else:
            self.teacher()
        QtCore.QMetaObject.connectSlotsByName(self)
    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "查询与修改", None))
        self.label_12.setText(_translate("self", "用户名", None))
        self.label_13.setText(_translate("self", "密码", None))
        self.label_14.setText(_translate("self", "姓名", None))
        self.label_15.setText(_translate("self", "电话", None))
        self.label_16.setText(_translate("self", "ID", None))
        self.label_17.setText(_translate("self", "出生日期", None))
        self.label_18.setText(_translate("self", "地址", None))
        self.pushButton.setText(_translate("self", "提交修改", None))
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'),self.change)
    def student(self):
        print(self.data)
        self.line_list = []
        print(self.data)
        y = 140
        for  student in self.data:
            user = QtGui.QLineEdit(self)
            user.setGeometry(QtCore.QRect(10, y, 113, 21))
            user.setObjectName(_fromUtf8("user"))
            user.setText(student[0])
            password = QtGui.QLineEdit(self)
            password.setGeometry(QtCore.QRect(123, y, 113, 21))
            password.setObjectName(_fromUtf8("password"))
            password.setText(student[1])
            ID = QtGui.QLineEdit(self)
            ID.setGeometry(QtCore.QRect(462, y, 113, 21))
            ID.setObjectName(_fromUtf8("ID"))
            ID.setText(student[4])
            name = QtGui.QLineEdit(self)
            name.setGeometry(QtCore.QRect(236, y, 113, 21))
            name.setObjectName(_fromUtf8("name"))
            name.setText(student[5])
            date = QtGui.QLineEdit(self)
            date.setGeometry(QtCore.QRect(575, y, 113, 21))
            date.setObjectName(_fromUtf8("date"))
            date.setText(student[7].strftime("%Y-%m-%d"))
            address = QtGui.QLineEdit(self)
            address.setGeometry(QtCore.QRect(688, y, 113, 21))
            address.setObjectName(_fromUtf8("address"))
            address.setText(student[6])
            phone = QtGui.QLineEdit(self)
            phone.setGeometry(QtCore.QRect(349, y, 113, 21))
            phone.setObjectName(_fromUtf8("phone"))
            phone.setText(student[8])
            li = [user,password,ID,name,date,address,phone]
            self.line_list.append(li)
            y+=21
    def teacher(self):
        y = 140
        self.line_list = []
        for teacher in self.data:
            user = QtGui.QLineEdit(self)
            user.setGeometry(QtCore.QRect(10, y, 113, 21))
            user.setObjectName(_fromUtf8("user"))
            user.setText(teacher[0])
            password = QtGui.QLineEdit(self)
            password.setGeometry(QtCore.QRect(123, y, 113, 21))
            password.setObjectName(_fromUtf8("password"))
            password.setText(teacher[1])
            name = QtGui.QLineEdit(self)
            name.setGeometry(QtCore.QRect(236, y, 113, 21))
            name.setObjectName(_fromUtf8("name"))
            name.setText(teacher[2])
            phone = QtGui.QLineEdit(self)
            phone.setGeometry(QtCore.QRect(349, y, 113, 21))
            phone.setObjectName(_fromUtf8("phone"))
            phone.setText(teacher[4])
            li = [user, password, name, phone]
            self.line_list.append(li)
    def change(self):
        data = []
        if  self.line_list == []:
            self.close()
            return
        if len(self.line_list[0]) == 4:
            for line in self.line_list:
                teacher = {
                    "user":line[0].text(),
                    "password":line[1].text(),
                    "name":line[2].text(),
                    "phone":line[3].text(),
                }
                data.append(teacher)
            fu.amend(data)
            self.close()
        else:
            for line in self.line_list:
                student = {
                    "user": line[0].text(),
                    "password": line[1].text(),
                    "ID":line[2].text(),
                    "name":line[3].text(),
                    "date":line[4].text(),
                    "address":line[5].text(),
                    "phone":line[6].text(),
                }
                data.append(student)
            fu.amend(data)
            self.close()







class Find_change(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('img/3.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        self.stu_user = QtGui.QLineEdit(self)
        self.stu_user.setGeometry(QtCore.QRect(132, 131, 191, 20))
        self.stu_user.setObjectName(_fromUtf8("stu_user"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(180, 90, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.stu_ID = QtGui.QLineEdit(self)
        self.stu_ID.setGeometry(QtCore.QRect(340, 130, 113, 21))
        self.stu_ID.setObjectName(_fromUtf8("stu_ID"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(370, 90, 72, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(510, 90, 72, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.stu_name = QtGui.QLineEdit(self)
        self.stu_name.setGeometry(QtCore.QRect(480, 130, 113, 21))
        self.stu_name.setObjectName(_fromUtf8("stu_name"))
        self.stu_adress = QtGui.QLineEdit(self)
        self.stu_adress.setGeometry(QtCore.QRect(620, 130, 113, 21))
        self.stu_adress.setObjectName(_fromUtf8("stu_adress"))
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(640, 90, 72, 15))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.stu_date = QtGui.QLineEdit(self)
        self.stu_date.setGeometry(QtCore.QRect(760, 130, 113, 21))
        self.stu_date.setText(_fromUtf8(""))
        self.stu_date.setObjectName(_fromUtf8("stu_date"))
        self.label_6 = QtGui.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(770, 90, 72, 15))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.stu_phone = QtGui.QLineEdit(self)
        self.stu_phone.setGeometry(QtCore.QRect(910, 130, 113, 21))
        self.stu_phone.setObjectName(_fromUtf8("stu_phone"))
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(930, 90, 72, 15))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.toolButton = QtGui.QToolButton(self)
        self.toolButton.setGeometry(QtCore.QRect(1050, 130, 47, 21))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.label_8 = QtGui.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(50, 190, 72, 15))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(180, 170, 72, 15))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tea_user = QtGui.QLineEdit(self)
        self.tea_user.setGeometry(QtCore.QRect(130, 190, 191, 20))
        self.tea_user.setObjectName(_fromUtf8("tea_user"))
        self.label_10 = QtGui.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(360, 170, 72, 15))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.tea_name = QtGui.QLineEdit(self)
        self.tea_name.setGeometry(QtCore.QRect(340, 190, 113, 21))
        self.tea_name.setObjectName(_fromUtf8("tea_name"))
        self.tea_phone = QtGui.QLineEdit(self)
        self.tea_phone.setGeometry(QtCore.QRect(480, 190, 113, 21))
        self.tea_phone.setObjectName(_fromUtf8("tea_phone"))
        self.label_11 = QtGui.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(510, 170, 72, 15))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.toolButton_2 = QtGui.QToolButton(self)
        self.toolButton_2.setGeometry(QtCore.QRect(1050, 190, 47, 21))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 260, 16, 101))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_2 = QtGui.QWidget(self)
        self.widget_2.setGeometry(QtCore.QRect(0, 290, 1111, 611))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.retranslateUi()
        self.connect_fun()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "查询", None))
        self.stu_user.setText(_translate("self", "有，则后面数据无效", None))
        self.label.setText(_translate("self", "用户名", None))
        self.label_2.setText(_translate("self", "学生", None))
        self.label_3.setText(_translate("self", "ID", None))
        self.label_4.setText(_translate("self", "名字", None))
        self.label_5.setText(_translate("self", "地址", None))
        self.label_6.setText(_translate("self", "出生日期", None))
        self.label_7.setText(_translate("self", "电话", None))
        self.toolButton.setText(_translate("self", "查找", None))
        self.label_8.setText(_translate("self", "老师", None))
        self.label_9.setText(_translate("self", "用户名", None))
        self.tea_user.setText(_translate("self", "有，则后面数据无效", None))
        self.label_10.setText(_translate("self", "姓名", None))
        self.label_11.setText(_translate("self", "电话", None))
        self.toolButton_2.setText(_translate("self", "查找", None))

    def connect_fun(self):

        self.connect(self.toolButton,QtCore.SIGNAL('clicked()'),self.func1)
        self.connect(self.toolButton_2,QtCore.SIGNAL('clicked()'),self.func2)

    def func1(self):
        stu_data = {
            "user": self.stu_user.text(),
            "ID": self.stu_ID.text(),
            "name": self.stu_name.text(),
            "address": self.stu_adress.text(),
            "life": self.stu_date.text(),
            "phone": self.stu_phone.text(),
        }
        data = fu.look_up("student", stu_data)
        self.am = amend("student", data)
        self.am.show()
        print("展示")
    def func2(self):
        tea_data = {"user": self.tea_user.text(),
                    "name": self.tea_name.text(),
                    "phone": self.tea_phone.text(),
                    }
        data = fu.look_up("teacher", tea_data)
        self.am = amend("teacher", data)
        self.am.show()


class Add(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('img/1.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        self.stu_user = QtGui.QLineEdit(self)
        self.stu_user.setGeometry(QtCore.QRect(230, 100, 113, 21))
        self.stu_user.setObjectName(_fromUtf8("stu_user"))
        self.stu_password = QtGui.QLineEdit(self)
        self.stu_password.setGeometry(QtCore.QRect(230, 140, 113, 21))
        self.stu_password.setObjectName(_fromUtf8("stu_password"))
        self.stu_ID = QtGui.QLineEdit(self)
        self.stu_ID.setGeometry(QtCore.QRect(230, 180, 113, 21))
        self.stu_ID.setObjectName(_fromUtf8("stu_ID"))
        self.stu_name = QtGui.QLineEdit(self)
        self.stu_name.setGeometry(QtCore.QRect(230, 220, 113, 21))
        self.stu_name.setObjectName(_fromUtf8("stu_name"))
        self.stu_add = QtGui.QLineEdit(self)
        self.stu_add.setGeometry(QtCore.QRect(230, 270, 113, 21))
        self.stu_add.setObjectName(_fromUtf8("stu_add"))
        self.stu_date = QtGui.QLineEdit(self)
        self.stu_date.setGeometry(QtCore.QRect(230, 320, 113, 21))
        self.stu_date.setObjectName(_fromUtf8("stu_date"))
        self.stu_phone = QtGui.QLineEdit(self)
        self.stu_phone.setGeometry(QtCore.QRect(230, 370, 113, 21))
        self.stu_phone.setObjectName(_fromUtf8("stu_phone"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(80, 100, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(80, 180, 72, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(80, 230, 72, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(80, 270, 72, 15))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(70, 320, 72, 15))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(80, 370, 72, 15))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(80, 30, 101, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 460, 101, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tea_user = QtGui.QLineEdit(self)
        self.tea_user.setGeometry(QtCore.QRect(230, 520, 113, 21))
        self.tea_user.setObjectName(_fromUtf8("tea_name"))
        self.tea_name = QtGui.QLineEdit(self)
        self.tea_name .setGeometry(QtCore.QRect(230,550,113,21))
        self.tl = QtGui.QLabel(self)
        self.tl.setGeometry(70,550,113,21)
        self.tl.setText("老师姓名")
        self.tea_pwd = QtGui.QLineEdit(self)
        self.tea_pwd.setGeometry(QtCore.QRect(230, 580, 113, 21))
        self.tea_pwd.setObjectName(_fromUtf8("tea_pwd"))
        self.label_8 = QtGui.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(70, 520, 72, 15))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(70, 580, 72, 15))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(70, 610, 72, 15))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.tea_phone = QtGui.QLineEdit(self)
        self.tea_phone.setGeometry(QtCore.QRect(230, 610, 113, 21))
        self.tea_phone.setObjectName(_fromUtf8("tea_phone"))
        self.photo = QtGui.QLineEdit(self)
        self.photo.setGeometry(QtCore.QRect(230, 640, 113, 21))
        self.photo.setObjectName(_fromUtf8("photo"))
        self.label_11 = QtGui.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(71,640, 71, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "self", None))
        self.label.setText(_translate("self", "用户名：", None))
        self.label_2.setText(_translate("self", "密码：", None))
        self.label_3.setText(_translate("self", "ID：", None))
        self.label_4.setText(_translate("self", "姓名：", None))
        self.label_5.setText(_translate("self", "地址：", None))
        self.label_6.setText(_translate("self", "出生日期：", None))
        self.label_7.setText(_translate("self", "电话：", None))
        self.pushButton.setText(_translate("self", "创建一个学生", None))
        self.pushButton_2.setText(_translate("self", "创建一个老师", None))
        self.label_8.setText(_translate("self", "用户名：", None))
        self.label_9.setText(_translate("self", "密码：", None))
        self.label_10.setText(_translate("self", "电话：", None))
        self.label_11.setText(_translate("self", "照片url", None))
        self.conncet_fun()

    def conncet_fun(self):
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.create_stu)
        self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.create_tea)

    def create_stu(self):
        data = {
            "user": self.stu_user.text(),
            "password": self.stu_password.text(),
            "date": time.strftime("%Y-%m-%d", time.localtime()),
            "identity": "student",
            "ID": self.stu_ID.text(),
            "name": self.stu_name.text(),
            "address": self.stu_add.text(),
            "life": self.stu_date.text(),
            "phone": self.stu_phone.text(),
        }
        sign = fu.creat_stu(data)
        if sign =="已存在":
            reply = QtGui.QMessageBox.question(self, '创建失败', "用户已存在", "确定")
    def create_tea(self):
        data = {
            "user":self.tea_user.text(),
            "password": self.tea_pwd.text(),
            "name":self.tea_name.text(),
            "identity":"teacher",
            "phone":self.tea_phone.text(),
            "img":self.photo.text(),
        }
        sign = fu.creat_tea(data)
        if sign == "已存在":
            reply = QtGui.QMessageBox.question(self, '创建失败', "用户已存在", "确定")


class Re(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('img/2.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(550, 340, 113, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(340, 340, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(440, 430, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "self", None))
        self.label.setText(_translate("self", "要删除对象的用户名：", None))
        self.pushButton.setText(_translate("self", "删除", None))
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.remove)

    def remove(self):
        ret = fu.delete(self.lineEdit.text())
        if ret == "NO this user":
            reply = QtGui.QMessageBox.question(self, '删除失败', "此用户不存在", "确定")
        else:
            reply = QtGui.QMessageBox.question(self, '成功', "此用户被删除", "确定")


