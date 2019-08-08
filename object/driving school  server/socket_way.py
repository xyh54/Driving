"""
@file:   socket_way.py
@date:   2019/04/16
"""
import os
import  sys
import socket
import select
import json
from mysqlsever import DB
from file_use import FileOperation
path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)
v_dir  = "./video"
t_dir  ="./test"
def enter(data):   #data样式(user,password)
    db = DB()
    acc_inf = db.find(data[0])
    if acc_inf  == None:
        return None
    if acc_inf[1] == data[1]:
        acc_inf[2]=f"{acc_inf[2].year}-{acc_inf[2].month}-{acc_inf[2].day}"
        acc_inf = bytes(json.dumps(acc_inf),encoding='utf8')
        return acc_inf      # 返回登入者的信息（）元祖
    else:
        return bytes("password_error")
def sign_in(data):              #data数据为{user:"sdf",password:"sfsadf"}
    db = DB()
    if db.find(data["user"]) is None:
        db.write_bd(data)
        acc_inf = db.find(data["user"])
        acc_inf = json.dumps(acc_inf)
        acc_inf = bytes(acc_inf)
        return acc_inf              #注册成功返回传入的字典
    else:
        return "already_exist"
def get_alltea(data):
    db = DB()
    return bytes(json.dumps(db.input_all("teather_tal")))           #返回为[]所有老师数据
def appointment_time(data):
    db = DB()
    return db.amend(data)

file_op = FileOperation()        #文件操作类FileOperation对象
#功能菜单
menu = {"enter":enter,                  #登入请求处理
        "sign_in":sign_in,              #注册请求处理
        "file_download":file_op.file_download,   #视频文件下载需求的文件操作
        "test_download":file_op.test_download,      #科一考试文件下载需求的文件操作
        "file_uploading":file_op.file_uploading,     #视频文件上传需求的文件操作
        "test_uploading":file_op.test_uploading,        #科一考试文件上传需求的文件操作
        "cat_video":file_op.cat_video,               #返回所有视频文件名
        "cat_test":file_op.cat_test,                  # 返回所有科一考试文件名
        "get_alltea" : get_alltea,                   #
        "appointment_time":appointment_time
        }
#服务器主体，通信功能
sk1 = socket.socket()
sk1.bind(('192.168.43.209', 8001))
sk1.listen()
inputs = [sk1, ]
outputs = []
message_dict = {}
data = ''
while True:
    r_list, w_list, e_list = select.select(inputs,[],[])
    for sk in r_list:
        #新用户发来请求
        if sk is sk1:
            conn,adress = sk1.accept()
            inputs.append(conn)
        else:
            try:
                sign = sk.recv(1024)      #旧用户请求
                sign = sign.decode(encoding="utf-8")        # 二进制转字符串
                sign = json.loads(sign)
                if sign[0] == "file_uploading" or sign[0] == "test_uploading":   #判断是否为大文件上传操作
                    sk.sendall(bytes("OK"))    #服务端发送"OK",提示客户端可以发送数据
                    ret = sk.recv(1024)
                    up_iter = menu(sign[0])(sign[1],ret)
                    num = up_iter.__next__
                    while True:
                        ret = sk.recv(1024)             #将大文件1M为单位传输
                        if ret == '':
                            print('传输结束')                  #判断客户端数据读取完毕
                            break
                        else:
                            num=up_iter.send(ret)
                else:
                    sk.sendall(bytes("OK",encoding='utf8'))
                    data = sk.recv(1024)                      #非大数据操作1M绰绰有余
            except Exception  as ex:                      #用于判断用户端是否断开连接，断开则删除套接字
                inputs.remove(sk)
            else:
                data=data.decode(encoding="utf-8")
                data = json.loads(data)         #json 反序列化
                print(data)
                if sign[0] == "file_download" or sign[0] == "test_download":    #判断是否为大文件下载操作
                    f_iter = menu[sign[0]](data)
                    for buf in f_iter:                                        #使用生成的文件迭代器发送文件数据
                        sk.sendall(buf)
                elif sign[0] == "file_uploading" or sign[0] == "test_uploading":
                        sk.sendall("finish")
                else:
                    ret_data=menu[sign[0]](data)      #发送回客户端的信息
                    sk.sendall(ret_data)










