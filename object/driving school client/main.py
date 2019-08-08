"""
@file:   main.py
@date:   2019/04/18
"""
import requests as req
import time, json, os, sys
import xlwt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
import sys

from multiprocessing import Process


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(479, 547)
        self.textout = QtWidgets.QTextBrowser(Form)
        self.textout.setGeometry(QtCore.QRect(20, 251, 431, 271))
        self.textout.setObjectName("textout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 20, 101, 31))
        self.label.setObjectName("label")
        self.lujinuot = QtWidgets.QLabel(Form)
        self.lujinuot.setGeometry(QtCore.QRect(90, 70, 271, 20))
        self.lujinuot.setObjectName("lujinuot")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.label_3.setObjectName("label_3")
        self.selectfile = QtWidgets.QPushButton(Form)
        self.selectfile.setGeometry(QtCore.QRect(370, 70, 81, 23))
        self.selectfile.setObjectName("selectfile")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 54, 12))
        self.label_4.setObjectName("label_4")
        self.incookie = QtWidgets.QLineEdit(Form)
        self.incookie.setGeometry(QtCore.QRect(70, 120, 381, 21))
        self.incookie.setObjectName("incookie")
        self.startpachong = QtWidgets.QPushButton(Form)
        self.startpachong.setGeometry(QtCore.QRect(20, 190, 431, 41))
        self.startpachong.setObjectName("startpachong")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "拼多多资料采集程序 v1.0"))
        self.label.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">程序设置</span></p></body></html>"))
        self.lujinuot.setText(_translate("Form", "路径显示"))
        self.label_3.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">保存路径</span></p></body></html>"))
        self.selectfile.setText(_translate("Form", "选择文件"))
        self.label_4.setText(_translate("Form", "cookie："))
        self.startpachong.setText(_translate("Form", "开始"))


def writeWFH(headers):
    filename = "未发货-" + str(time.strftime("%Y-%m-%d").strip()) + ".xls"
    # filename = os.path.join(ui.lujinuot.text(),filename)
    wbk = xlwt.Workbook()
    ws = wbk.add_sheet('sheet 1')
    ws.write(0, 0, "昵称")
    ws.write(0, 1, "电话号码")
    ws.write(0, 2, "地址")
    ws.write(0, 3, "快递公司")
    ws.write(0, 4, "快递单号")

    count = 1
    page = 1
    while True:
        url = "https://st.huanleguang.com/api/trades?status=paid&print_status=all&shipping_delay=all&shop_id=&memo_type=1&seller_flag=-1&refund_status=all&order_type=all&area_info=all&order_num=all&post_type=all&merge_type=all&trade_type=all&page_size=200&page_no=%s&tid=&buyer_nick=&express_no=&receiver_mobile=&receiver_name=&item_name_id=&sku_size=&sku_color=" % page
        ret = req.get(url=url, headers=headers)
        if len(json.loads(ret.text)) > 0:
            for line in json.loads(ret.text):
                TextWrite("第 %s 条记录" % count)
                line = line[0]
                nickname = line["receiver_name"]
                phone = line["receiver_mobile"]
                add = line["receiver_state"] + line["receiver_city"] + line["receiver_district"] + line[
                    "receiver_address"]
                kuaidi = line["express_name"]
                danhao = line["express_no"]
                ws.write(count, 0, nickname)
                ws.write(count, 1, phone)
                ws.write(count, 2, add)
                ws.write(count, 3, kuaidi)
                ws.write(count, 4, danhao)
                count = count + 1
            page = page + 1
        else:
            wbk.save(filename)
            TextWrite("保存成功！%s" % filename)
            break
            return


def writeYFH(headers):
    wbk = xlwt.Workbook()
    ws = wbk.add_sheet('sheet 1')
    ws.write(0, 0, "昵称")
    ws.write(0, 1, "电话号码")
    ws.write(0, 2, "地址")
    ws.write(0, 3, "快递公司")
    ws.write(0, 4, "快递单号")

    filename = "已发货-%s.xls" % str(time.strftime("%Y-%m-%d").strip())
    # filename = os.path.join(ui.lujinuot.text(),filename)
    count = 1
    page = 1
    while True:
        url = "https://st.huanleguang.com/api/trades?status=shipped&print_status=all&shipping_delay=all&shop_id=&memo_type=1&seller_flag=-1&refund_status=all&order_type=all&area_info=all&order_num=all&post_type=all&merge_type=all&trade_type=all&page_size=200&page_no=%s&tid=&buyer_nick=&express_no=&receiver_mobile=&receiver_name=&item_name_id=&sku_size=&sku_color=" % page
        ret = req.get(url=url, headers=headers)
        if len(json.loads(ret.text)) > 0:
            for line in json.loads(ret.text):
                TextWrite("第 %s 条记录" % count)
                line = line[0]
                nickname = line["receiver_name"]
                phone = line["receiver_mobile"]
                add = line["receiver_state"] + line["receiver_city"] + line["receiver_district"] + line[
                    "receiver_address"]
                kuaidi = line["express_name"]
                danhao = line["express_no"]
                ws.write(count, 0, nickname)
                ws.write(count, 1, phone)
                ws.write(count, 2, add)
                ws.write(count, 3, kuaidi)
                ws.write(count, 4, danhao)
                count = count + 1
            page = page + 1
        else:
            wbk.save(filename)
            TextWrite("保存成功！%s" % filename)
            return


def SelectFile():
    filename = QFileDialog.getExistingDirectory()
    ui.lujinuot.setText(filename)


def TextWrite(msg):
    ui.textout.append(str(msg))
    print(msg)
    QtWidgets.QApplication.processEvents()


def pa():
    cookie = ui.lujinuot.text().strip()
    # cookie = "__guid=227988319.2581628879631838000.1540522358017.8997; gr_user_id=b83ae182-83cd-4b7e-84b0-c22e856d1c3d; gr_session_id_84652f4a0b894385=7ef6971a-1053-47b0-bc0d-2eb931e3ed88; gr_session_id_84652f4a0b894385_7ef6971a-1053-47b0-bc0d-2eb931e3ed88=true; hlg_8_0=8-5045059-3-e695f708efb6c3e814ec42de4798554f; monitor_count=2; gr_cs1_7ef6971a-1053-47b0-bc0d-2eb931e3ed88=shop_id%3A5045059; _ati=7213780759932"

    headers = {"Accept-Encoding": "gzip, deflate, br", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "keep-alive",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
               "Cookie": cookie}
    # 全部数据
    try:
        time1 = time.time()
        writeWFH(headers)
        writeYFH(headers)
        time2 = time.time()
        time3 = time2 - time1
        TextWrite("用时 %s 秒" % str(int(time3 * 10) / 10))
    except Exception as e:
        TextWrite("访问出错！" + str(e))


def StartPa():
    # TextWrite(ui.incookie.text())
    if ui.lujinuot.text() == "路径显示":
        TextWrite("<html><head/><body><span style=\" color:red;\">请先选择文件保存路径!!!</span></body></html>")
        return
    elif ui.lujinuot.text() == "":
        TextWrite("<html><head/><body><span style=\" color:red;\">保存路径不能为空!!!</span></body></html>")
        return
    elif ui.incookie.text() == "":
        TextWrite("<html><head/><body><span style=\" color:red;\">cookie不能为空!!!</span></body></html>")
        return
    else:
        pa()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.selectfile.clicked.connect(SelectFile)
    ui.startpachong.clicked.connect(StartPa)

    sys.exit(app.exec_())
