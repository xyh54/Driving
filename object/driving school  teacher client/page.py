# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'ui_name.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

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

class Show_inf(QtGui.QWidget):
    def __init__(self,account):
        super().__init__()
        self.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/1.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        self.account = account
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(430, 110, 191, 181))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(320, 330, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(320, 400, 72, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(320, 470, 72, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.user = QtGui.QLabel(self)
        self.user.setGeometry(QtCore.QRect(500, 330, 72, 15))
        self.user.setText(_fromUtf8(""))
        self.user.setObjectName(_fromUtf8("user"))
        self.name = QtGui.QLabel(self)
        self.name.setGeometry(QtCore.QRect(500, 400, 72, 15))
        self.name.setText(_fromUtf8(""))
        self.name.setObjectName(_fromUtf8("name"))
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(500, 470, 72, 15))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "老师信息", None))
        self.label_2.setText(_translate("self", "用户名", None))
        self.label_3.setText(_translate("self", "姓名", None))
        self.label_4.setText(_translate("self", "电话", None))
        png = QtGui.QPixmap(_fromUtf8(self.account[5])).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(png)
        self.user.setText(self.account[0])
        self.name.setText(self.account[2])
        self.label_7.setText(self.account[4])
class Uploading(QtGui.QWidget):
    def __init__(self,cl):
        super().__init__()
        self.cl = cl
        self.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/2.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 170, 93, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 70, 300, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QLineEdit(self)
        self.line.setGeometry(QtCore.QRect(30, 120, 191, 31))
        self.line.setText("填写文件名")
        self.retranslateUi()
        self.connectfun()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, ):
        self.setWindowTitle(_translate("self", "视频上传", None))
        self.pushButton.setText(_translate("self", "选择上传文件", None))
        self.pushButton_2.setText(_translate("self", "上传", None))
        self.label.setText(_translate("self", "上传文件路径", None))
    def connectfun(self):
        self.connect(self.pushButton_2,QtCore.SIGNAL('clicked()'),self.uploading)
        self.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.find_file)

    def find_file(self):
        path = QtGui.QFileDialog.getOpenFileName(self, u'打开文件', './')
        self.label.setText(path)
    def uploading(self):
        if self.label.text() == "上传文件名" or self.line.text() == "填写文件名":
            reply = QtGui.QMessageBox.question(self, '上传失败', "必须要有文件路径与上传文件名", "确定")
        else:
            progressDialog = QtGui.QProgressDialog(self)
            progressDialog.setWindowModality(QtCore.Qt.WindowModal)
            progressDialog.setMinimumDuration(5)
            progressDialog.setWindowTitle("请等待")
            progressDialog.setLabelText("上传中...")
            progressDialog.setCancelButtonText("取消")
            progressDialog.setRange(0, 100)
            iter1 = self.cl.video_uploading(self.label.text(), self.line.text())
            filesize =  int(os.path.getsize(self.label.text())/1024)
            for schedule in iter1:
                print(schedule)
                print(filesize)
                print(int(schedule / filesize * 100))
                progressDialog.setValue(int(schedule / filesize * 100))

class Appointment(QtGui.QWidget):
    def __init__(self,account):
        super().__init__()
        self.account = account
        self.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/3.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(300, 300, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(300, 270, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(300, 340, 72, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(300, 380, 72, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(300, 420, 72, 15))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(300, 450, 72, 15))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.am9 = QtGui.QLabel(self)
        self.am9.setGeometry(QtCore.QRect(450, 270, 72, 15))
        self.am9.setText(_fromUtf8(""))
        self.am9.setObjectName(_fromUtf8("am9"))
        self.am10 = QtGui.QLabel(self)
        self.am10.setGeometry(QtCore.QRect(450, 300, 72, 15))
        self.am10.setText(_fromUtf8(""))
        self.am10.setObjectName(_fromUtf8("am10"))
        self.am11 = QtGui.QLabel(self)
        self.am11.setGeometry(QtCore.QRect(450, 340, 72, 15))
        self.am11.setText(_fromUtf8(""))
        self.am11.setObjectName(_fromUtf8("am11"))
        self.pm3 = QtGui.QLabel(self)
        self.pm3.setGeometry(QtCore.QRect(450, 380, 72, 15))
        self.pm3.setText(_fromUtf8(""))
        self.pm3.setObjectName(_fromUtf8("pm3"))
        self.pm4 = QtGui.QLabel(self)
        self.pm4.setGeometry(QtCore.QRect(450, 420, 72, 15))
        self.pm4.setText(_fromUtf8(""))
        self.pm4.setObjectName(_fromUtf8("pm4"))
        self.label_12 = QtGui.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(450, 450, 72, 15))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "self", None))
        self.label.setText(_translate("self", "上午10点：", None))
        self.label_2.setText(_translate("self", "上午9点：", None))
        self.label_3.setText(_translate("self", "上午11点：", None))
        self.label_4.setText(_translate("self", "下午3点", None))
        self.label_5.setText(_translate("self", "下午4点", None))
        self.label_6.setText(_translate("self", "下午5点", None))
        self.am9.setText(self.account[8])
        self.am10.setText(self.account[9])
        self.am11.setText(self.account[10])
        self.pm3.setText(self.account[11])
        self.pm4.setText(self.account[12])
        self.label_12.setText(self.account[13])

class Cat_stu(QtGui.QWidget):
    def __init__(self,cl):
        super().__init__()
        self.cl = cl
        self.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/4.jpg')))  # 设置背景图片
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
        self.label.setText(_translate("self", "要查询对象的用户名：", None))
        self.pushButton.setText(_translate("self", "查询", None))
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.cat_stu)

    def cat_stu(self):
        ret = self.cl.cat_stu(self.lineEdit.text())
        if  ret != None:
            self.reply = QtGui.QMessageBox.question(self, '学生数据', f"用户名：{ret[0]}\n姓名：{ret[5]}\n电话：{ret[8]}", "确定")
        else:
            self.reply = QtGui.QMessageBox.question(self, '查询出错', f"没有这个学生", "确定")
