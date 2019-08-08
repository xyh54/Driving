# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_name.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from  account import *

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

class Teacher_app(QtGui.QWidget):
    def __init__(self,cl,teacher,allteacher):
        super().__init__()
        self.cl = cl
        self.teachers = allteacher
        self.account = cl.account
        self.teacher = teacher
        self.setWindowTitle("预约")
        self.setGeometry(300,300,200,400)
        self.toolbuttonlist = []
        self.groupboxlist = []
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/1.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        toolButton1 =QtGui.QToolButton()
        toolButton1.setText(self.tr(f"{teacher[8]}"))
        toolButton1.setIcon(QtGui.QIcon("icon/biao.png"))
        toolButton1.setIconSize(QtCore.QSize(40, 40))
        toolButton1.setAutoRaise(True)
        toolButton1.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolbuttonlist.append(toolButton1)

        toolButton2 = QtGui.QToolButton()
        toolButton2.setText(self.tr(f"{teacher[9]}"))
        toolButton2.setIcon(QtGui.QIcon("icon/biao.png"))
        toolButton2.setIconSize(QtCore.QSize(40, 40))
        toolButton2.setAutoRaise(True)
        toolButton2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolbuttonlist.append(toolButton2)

        toolButton3 = QtGui.QToolButton()
        toolButton3.setText(self.tr(f"{teacher[10]}"))
        toolButton3.setIcon(QtGui.QIcon("icon/biao.png"))
        toolButton3.setIconSize(QtCore.QSize(40, 40))
        toolButton3.setAutoRaise(True)
        toolButton3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolbuttonlist.append(toolButton3)

        toolButton4 = QtGui.QToolButton()
        toolButton4.setText(self.tr(f"{teacher[11]}"))
        toolButton4.setIcon(QtGui.QIcon("icon/biao.png"))
        toolButton4.setIconSize(QtCore.QSize(40, 40))
        toolButton4.setAutoRaise(True)
        toolButton4.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolbuttonlist.append(toolButton4)

        toolButton5 = QtGui.QToolButton()
        toolButton5.setText(self.tr(f"{teacher[11]}"))
        toolButton5.setIcon(QtGui.QIcon("icon/biao.png"))
        toolButton5.setIconSize(QtCore.QSize(40, 40))
        toolButton5.setAutoRaise(True)
        toolButton5.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolbuttonlist.append(toolButton5)

        toolButton6 = QtGui.QToolButton()
        toolButton6.setText(self.tr(f"{teacher[12]}"))
        toolButton6.setIcon(QtGui.QIcon("icon/biao.png"))
        toolButton6.setIconSize(QtCore.QSize(40, 40))
        toolButton6.setAutoRaise(True)
        toolButton6.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolbuttonlist.append(toolButton6)


        groupbox1 = QtGui.QGroupBox()
        vlayout1 = QtGui.QVBoxLayout(groupbox1)
        vlayout1.setMargin(10)
        vlayout1.setAlignment(QtCore.Qt.AlignCenter)
        vlayout1.addWidget(toolButton1)
        vlayout1.addStretch()
        self.groupboxlist.append(groupbox1)

        groupbox2 = QtGui.QGroupBox()
        vlayout2 = QtGui.QVBoxLayout(groupbox2)
        vlayout2.setMargin(10)
        vlayout2.setAlignment(QtCore.Qt.AlignCenter)
        vlayout2.addWidget(toolButton2)
        vlayout2.addStretch()
        self.groupboxlist.append(groupbox2)

        groupbox3 = QtGui.QGroupBox()
        vlayout3 = QtGui.QVBoxLayout(groupbox3)
        vlayout3.setMargin(10)
        vlayout3.setAlignment(QtCore.Qt.AlignCenter)
        vlayout3.addWidget(toolButton3)
        vlayout3.addStretch()
        self.groupboxlist.append(groupbox3)

        groupbox4 = QtGui.QGroupBox()
        vlayout4 = QtGui.QVBoxLayout(groupbox4)
        vlayout4.setMargin(10)
        vlayout4.setAlignment(QtCore.Qt.AlignCenter)
        vlayout4.addWidget(toolButton4)
        vlayout4.addStretch()
        self.groupboxlist.append(groupbox4)

        groupbox5 = QtGui.QGroupBox()
        vlayout5 = QtGui.QVBoxLayout(groupbox5)
        vlayout5.setMargin(10)
        vlayout5.setAlignment(QtCore.Qt.AlignCenter)
        vlayout5.addWidget(toolButton5)
        vlayout5.addStretch()
        self.groupboxlist.append(groupbox5)

        groupbox6 = QtGui.QGroupBox()
        vlayout6 = QtGui.QVBoxLayout(groupbox6)
        vlayout6.setMargin(10)
        vlayout6.setAlignment(QtCore.Qt.AlignCenter)
        vlayout6.addWidget(toolButton6)
        vlayout6.addStretch()
        self.groupboxlist.append(groupbox6)

        toolbox1 = QtGui.QToolBox(self)
        toolbox1.addItem(groupbox1, "am9点")
        toolbox1.addItem(groupbox2, "am10点")
        toolbox1.addItem(groupbox3, "am11点")
        toolbox1.addItem(groupbox4, "pm3点")
        toolbox1.addItem(groupbox5, "pm4点")
        toolbox1.addItem(groupbox6, "pm5点")
        li = ["am9","am10","am11","pm3","pm4","pm5"]
        for  i  in range(len(self.toolbuttonlist)):
            app_time = self.func(li[i],self.teacher[6],self.toolbuttonlist[i])
            self.groupboxlist[i].connect(self.toolbuttonlist[i],QtCore.SIGNAL("clicked()"),app_time)

    def func(self,time,id,button):
        def app_time():
            print("按钮",button.text())
            for teacher in self.teachers:
                if self.account.user  in teacher[8:14]:
                    self.reply = QtGui.QMessageBox.question(self, '预约失败', f"您今天已经预约过了", "确定")
                    break
            else:
                if  button.text()  !=  "None" and button.text()!= '':
                    self.reply = QtGui.QMessageBox.question(self, '预约失败', f"已经有人预约这个时间了，请重新选择", "确定")
                else:
                    self.cl.appointment_time(time,self.cl.account.user,id)
                    button.setText(f"{self.cl.account.user}")
        return app_time





class Apply(QtGui.QWidget):
    def __init__(self,cl):
        super().__init__()
        self.cl=cl
        self.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/6.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(330, 110, 451, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(470, 520, 141, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(310, 200, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(310, 240, 72, 15))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(310, 230, 72, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(310, 260, 72, 15))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(310, 290, 72, 15))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(310, 320, 72, 15))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(460, 200, 201, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 230, 201, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(460, 260, 201, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(460, 290, 201, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(460, 320, 201, 21))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.retranslateUi()
        self.connect(self.pushButton,QtCore.SIGNAL('clicked()'), self.become_student)
        QtCore.QMetaObject.connectSlotsByName(self)
    def retranslateUi(self):
        self.label.setText(_translate("self", "                    阳光驾校报名", None))
        self.pushButton.setText(_translate("self", "报名", None))
        self.label_2.setText(_translate("self", "身份证号：", None))
        self.label_4.setText(_translate("self", "名字    ：", None))
        self.label_5.setText(_translate("self", "地址    : ", None))
        self.label_6.setText(_translate("self", "出生日期：", None))
        self.label_7.setText(_translate("self", "电话   :", None))
    def become_student(self):
        if  self.cl.account.identity == "student":
            reply = QtGui.QMessageBox.question(self, '非法操作', "你已经是驾校学员", "确定")
        data = {"user":self.cl.account.user,"password":self.cl.account.pwd,"date":"2004-05-23","identity":self.cl.account.identity}
        data.update({"ID":self.lineEdit.text(),"name":self.lineEdit_2.text(),"address":self.lineEdit_3.text(),"life":self.lineEdit_4.text(),"phone":self.lineEdit_5.text()})
        print(type(data))
        self.cl.promote_stu(data)

class download_video(QtGui.QScrollArea):
    def __init__(self,cl,filenames):
        super().__init__()
        self.cl = cl
        self.filenames = filenames
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/7.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        if filenames != "permission denied":
            self.retranslateUi()
        else:
            self.errorlabel = QtGui.QLabel(self)
            self.errorlabel.setText("由于你是非学员用户，没有权限获取此页面信息")
            self.errorlabel.resize(350,250)
            screen = self.geometry()     # 获取窗口的像素大小
            size = self.errorlabel.geometry()  # 获取窗口的像素大小
            self.errorlabel.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
    def retranslateUi(self):
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 111, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setText("video")
        self.label_2.setGeometry(QtCore.QRect(200, 80, 300, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.file()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setWindowTitle(_translate("self", "self", None))
        self.pushButton.setText(_translate("self", "选择存储路径", None))
        self.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.mk_dir)
    def mk_dir(self):
        dir_path = QtGui.QFileDialog.getExistingDirectory(self, "choose directory", "./")
        self.label_2.setText(dir_path)
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.yellow)
        self.label_2.setPalette(pe)
    def file(self):
        x = 20
        y =160
        label_list = []
        toolButton_list = []
        groupBox_list = []
        print(self.filenames)
        for filename in self.filenames:
            groupBox = QtGui.QGroupBox(self)
            groupBox.setGeometry(QtCore.QRect(x, y, 120, 80))
            groupBox.setObjectName(_fromUtf8("groupBox"))
            label = QtGui.QLabel(groupBox)
            label.setGeometry(QtCore.QRect(20, 20, 72, 15))
            label.setText(filename)
            pe = QtGui.QPalette()
            pe.setColor(QtGui.QPalette.WindowText,QtCore.Qt.yellow)
            label.setPalette(pe)
            label.setObjectName(_fromUtf8("label"))
            toolButton = QtGui.QToolButton(groupBox)
            toolButton.setText("下载")
            toolButton.setGeometry(QtCore.QRect(30, 50, 47, 21))
            toolButton.setObjectName(_fromUtf8("toolButton"))
            label_list.append(label)
            toolButton_list.append(toolButton)
            groupBox_list.append(groupBox)
            x+=130
            if x>1100:
                x = 20
                y = y+90
        #lambda: self.download(label_list[num].text()
        for  num in  range(len(label_list)):
            print(label_list[num].text())
            print(label_list[num].text())
            fun = self.func(label_list[num].text())
            groupBox_list[num].connect(toolButton_list[num], QtCore.SIGNAL("clicked()"), fun)
    def func(self,filename):
        def download():
            if self.cl.account.identity == "visitor":
                self.reply = QtGui.QMessageBox.question(self, '权限缺失', f"您还不是驾校学员，要想预约老师请报名", "确定")
            else:
                progressDialog =QtGui.QProgressDialog(self)
                progressDialog.setWindowModality(QtCore.Qt.WindowModal)
                progressDialog.setMinimumDuration(5)
                progressDialog.setWindowTitle("请等待")
                progressDialog.setLabelText("下载中...")
                progressDialog.setCancelButtonText("取消")
                progressDialog.setRange(0, 100)
                load_iter = self.cl.download_video(self.label_2.text(), filename)
                filesize = int(int(load_iter.__next__()) / 1024)
                for schedule in load_iter:
                    print(int(schedule / filesize * 100))
                    progressDialog.setValue(int(schedule / filesize * 100))
        return  download

class Appointment(QtGui.QWidget):
    def __init__(self,cl,teachers):
        super().__init__()
        self.cl = cl
        self.account = cl.account
        self.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/5.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        self.teachers = teachers
        self.setObjectName(_fromUtf8("appointment"))
        self.allteacher()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "self", None))

    def allteacher(self):
        x = 20
        y = 160
        groupBoxlist = []
        toolButtonlist = []
        toolButton_2list = []
        print(self.teachers)
        for teacher in self.teachers:
            groupBox = QtGui.QGroupBox(self)
            groupBox.setTitle(_translate("self", teacher[2]+"老师", None))
            groupBox.setGeometry(QtCore.QRect(x, y, 251, 201))
            groupBoxlist.append(groupBox)
            label = QtGui.QLabel(groupBox)
            label.setGeometry(QtCore.QRect(60, 30, 121, 91))
            label.setObjectName(_fromUtf8("label"))
            png = QtGui.QPixmap(_fromUtf8(teacher[5])).scaled(label.width(),label.height())
            label.setPixmap(png)
            toolButton = QtGui.QToolButton(groupBox)
            toolButton.setText(_translate("self", "预约", None))
            toolButton.setGeometry(QtCore.QRect(20, 160, 47, 21))
            toolButton.setObjectName(_fromUtf8("toolButton"))
            toolButtonlist.append(toolButton)
            toolButton_2 = QtGui.QToolButton(groupBox)
            toolButton_2.setText(_translate("self", "查看", None))
            toolButton_2.setGeometry(QtCore.QRect(180, 160, 47, 21))
            toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
            toolButton_2list.append(toolButton_2)
            x += 260
            if x > 1100:
                x = 20
                y = y + 90
        for  i in range(len(groupBoxlist)):
            print(groupBoxlist[i].title())
            app_time = self.fun(groupBoxlist[i].title())
            show = self.tea_inf(groupBoxlist[i].title())
            groupBoxlist[i].connect(toolButtonlist[i],QtCore.SIGNAL("clicked()"),app_time)
            groupBoxlist[i].connect(toolButton_2list[i], QtCore.SIGNAL("clicked()"), show)
    def fun(self,teacher_name):
        def app_time():
            if self.account.identity == "visitor":
                self.reply = QtGui.QMessageBox.question(self, '权限缺失', f"您还不是驾校学员，要想预约老师请报名", "确定")
            else:
                for teacher in self.teachers:
                    if (teacher[2]+ "老师")== teacher_name:
                        self.ta = Teacher_app(self.cl,teacher,self.teachers)
                        self.ta.show()
        return app_time

    def tea_inf(self,teacher_name):
        def show():
            for teacher in self.teachers:
                if (teacher[2]+ "老师")== teacher_name:
                    self.reply = QtGui.QMessageBox.question(self, '老师电话', f"电话:{teacher[4]}", "确定")
        return show
class Answer(QtGui.QWidget):
    def __init__(self,widget,questions):
        super().__init__()
        self.widget = widget
        self.questions = questions
        self.question_list = []
        self.setWindowTitle("答题")
        self.setGeometry(300,300,1000,600)
        self.toolbox = QtGui.QToolBox(self)
        self.toolbox.resize(900,300)
        self.data=[]
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/1.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        for  question in self.questions:
            groupbox = QtGui.QGroupBox()
            # vlayout = QtGui.QVBoxLayout(groupbox)
            # vlayout.setMargin(10)
            # vlayout.setAlignment(QtCore.Qt.AlignCenter)
            a = QtGui.QRadioButton(groupbox)
            a.setText(question[2])
            a.setGeometry(0,0,30,30)
            b = QtGui.QRadioButton(groupbox)
            b.setText(question[3])
            b.setGeometry(0, 30, 30, 30)
            c= QtGui.QRadioButton(groupbox)
            c.setText(question[4])
            c.setGeometry(0,60,30,30)
            # vlayout.addWidget(a)
            # vlayout.addWidget(b)
            # vlayout.addWidget(c)
            # vlayout.addStretch()
            self.data .append([a,b,c])
            self.toolbox.addItem(groupbox,question[1])
        button  = QtGui.QPushButton(self)
        button.setText("提交")
        button.setGeometry(450,400,60,60)
        submit = self.func(self.data)
        self.connect(button,QtCore.SIGNAL('clicked()'), submit)
    def func(self,data):
        def submit():
            for   num in range(len(self.questions)):
                for i  in  range(3):
                    if data[num][i].isChecked():
                        if data[num][i].text() != self.questions[num][5]:
                            self.widget.error_num.setText(str(int(self.widget.error_num.text()) + 1))
                            self.question_list.append(self.questions[num])
                        break
                else:
                    self.widget.error_num.setText(str(int(self.widget.error_num.text()) + 1))
                    self.question_list.append(self.questions[num])
            self.widget.question_num.setText(str(int(self.widget.question_num.text()) + 5))
            p = ( int(self.widget.question_num.text())-int(self.widget.error_num.text()) )/int(self.widget.question_num.text())
            print(p)
            self.widget.accuracy.setText(f"{p*100}%")
            self.string = ''
            if self.question_list ==[]:
                self.reply = QtGui.QMessageBox.question(self, '恭喜', f"全部正确", "确定")
            else:
                for question in self.question_list:
                    self.string=self.string+f"题目:{question[1]}\n1.{question[2]}\n2.{question[3]}\n3.{question[4]}\n答案：{question[5]}\n"
                self.widget.label_3.setText(self.string)
            self.close()
        return submit




class test(QtGui.QWidget):
    def __init__(self,cl):
        super().__init__()
        self.cl=cl
        self.question_num = QtGui.QLabel(self)
        self.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/10.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        self.error_question = None
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(450, 400, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.question_num = QtGui.QLabel(self)
        self.question_num.setGeometry(QtCore.QRect(550, 400, 72, 15))
        self.question_num.setText(_fromUtf8(""))
        self.question_num.setObjectName(_fromUtf8("question_num"))
        self.question_num.setText("0")
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(500, 620, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 240, 400))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setText("这里是出错问题的正确答案")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('picture/8.jpg')))  # 设置背景图片
        self.label_3.setPalette(palette1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(420, 430, 72, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.error_num = QtGui.QLabel(self)
        self.error_num.setGeometry(QtCore.QRect(560, 430, 72, 21))
        self.error_num.setText(_fromUtf8(""))
        self.error_num.setObjectName(_fromUtf8("error_num"))
        self.error_num.setText("0")
        self.label_6 = QtGui.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(420, 470, 72, 15))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.accuracy = QtGui.QLabel(self)
        self.accuracy.setGeometry(QtCore.QRect(540, 470, 72, 15))
        self.accuracy.setText(_fromUtf8(""))
        self.accuracy.setObjectName(_fromUtf8("accuracy"))
        self.accuracy.setText("0")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "self", None))
        self.label.setText(_translate("self", "已答：", None))
        self.pushButton.setText(_translate("self", "答题", None))
        self.label_4.setText(_translate("self", "答错题数：", None))
        self.label_6.setText(_translate("self", "正确率", None))
        question = self.func(self,self.cl)
        self.connect(self.pushButton,QtCore.SIGNAL('clicked()'),question)
    def func(self,widget,cl):
        def question():
            questions = self.cl.test(5)
            a = Answer(widget,questions )
            a.show()
            print(self.error_question)
        return question









