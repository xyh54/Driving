"""
@file:   test.py
@date:   2019/04/18
"""
"""
@file:   socket_way.py
@date:   2019/04/16
"""
import os
import  sys
import socket
import select
import json
from  threading import  Thread
from mysqlsever import DB
from file_use import FileOperation
import time
import datetime
path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)
v_dir  = "./video"
t_dir  ="./test"
inputs = []
def enter(data):   #data样式(user,password)
    db = DB()
    print(data)
    acc_inf = db.find(data[0])
    print(acc_inf)
    if acc_inf  is None:
        return "account_error"
    if acc_inf[3] != "teacher":
        if acc_inf[1] == data[1]:
            acc_inf[2] = f"{acc_inf[2].year}-{acc_inf[2].month}-{acc_inf[2].day}"
            if acc_inf[3] == 'student':
                acc_inf[7] = f"{acc_inf[7].year}-{acc_inf[7].month}-{acc_inf[7].day}"
            return acc_inf      # 返回登入者的信息（）元祖
        else:
            return "account_error"
    else:
        if acc_inf[1] == data[1]:
            return acc_inf
        else:
            return  "account_error"
def sign_in(data):              #data数据为{user:"sdf",password:"sfsadf"..........}
    print(data)
    db = DB()
    if db.find(data["user"]) == []:
        db.write_bd(data)
        acc_inf = db.find(data["user"])
        acc_inf[2] = f"{acc_inf[2].year}-{acc_inf[2].month}-{acc_inf[2].day}"
        return acc_inf              #注册成功返回传入的字典
    else:
        return "already_exist"
def get_all(data):
    db = DB()
    return db.input_all(data)         #返回为[]所有老师数据
def appointment_time(data):
    db = DB()
    ret = db.add_app_stu(data)
    return ret
def promote_stu(data):
    db = DB()
    data["identity"] = "student"
    db.write_bd(data)
    db.delete(data["user"],"visitor_tal")
    ret = db.find(data["user"])
    ret[2] = f"{ret[2].year}-{ret[2].month}-{ret[2].day}"
    print(ret)
    return  ret
def img_synchronization(data):
    print("累了")
    ser_img = set()
    aco_img = set(data)
    for root, dirs, files in os.walk("img"):
        ser_img = set(files)
    li = list(ser_img - aco_img)
    return li
def test(data):
    db = DB()
    return db.test(data)
def cat_stu(user):
    db = DB()
    data = db.find(user)
    print(data)
    data[2] = data[2].strftime("%Y-%m-%d")
    data[7] = data[7].strftime("%Y-%m-%d")
    return data




file_op = FileOperation()        #文件操作类FileOperation对象
#功能菜单
menu = {"enter":enter,                  #登入请求处理
        "sign_in":sign_in,              #注册请求处理
        "file_download":file_op.file_download,   #视频文件下载需求的文件操作
        "file_uploading":file_op.file_uploading,     #视频文件上传需求的文件操作
        "cat_video":file_op.cat_video,               #返回所有视频文件名
        "cat_test":file_op.cat_test,                  # 返回所有科一考试文件名
        "get_all" : get_all,                   #
        "appointment_time":appointment_time,
        "promote_stu":promote_stu,
        "img_synchronization":img_synchronization,
        "get_img":file_op.img_download,
        "test":test,
        "cat_stu":cat_stu,
        }
#服务器主体，通信功能
def fun(sk):
    data = None
    n = 0
    while True:
        try:
            sign = sk.recv(1024)  # 子线程处理客户数据
            sign = sign.decode(encoding="utf-8")  # 二进制转字符串
            sign = json.loads(sign)  # 反序列化
            print(sign)
            # if  (sign[0] != "enter" and n == 0) and (sign[0] != "sign_in"  and n ==0):  #第一次不是登入注册马上断开
            #     print("在这")
            #     return None
            if sign[0] == "exit":
                return None
            elif sign[0] == "file_uploading" :  # 判断是否为大文件上传操作
                sk.sendall(bytes("OK",encoding="utf-8"))  # 服务端发送"OK",提示客户端可以发送数据
                ret = sk.recv(1024)
                up_iter = menu[sign[0]](sign[1], ret)
                num = up_iter.__next__()
                while len(ret) == 1024:
                    ret = sk.recv(1024)  # 将大文件1M为单位传输
                    num = up_iter.send(ret)
                    if len(ret) <1024 :
                        print('传输结束')  # 判断客户端数据读取完毕
                        break

            else:
                sk.sendall(bytes("OK", encoding='utf8'))
                data = sk.recv(1024)  # 非大数据操作1M绰绰有余
                data = data.decode("utf-8")  # 文本数据二进制转字符
                data = json.loads(data)
                print(data)
        except Exception  as ex:  # 用于判断用户端是否断开连接，断开则删除套接字
            return None
        else:
            try:
                if sign[0] == "file_download" :  # 判断是否为大文件下载操作
                    path = os.path.join("video",data)
                    size = os.path.getsize(path)
                    size = str(size)
                    size = json.dumps(size)

                    size = bytes(size, encoding='utf8')
                    sk.sendall(size)
                    print(size)
                    time.sleep(1)                  #等待两秒，让服务端获取文件大小
                    f_iter = menu[sign[0]](data)
                    num = 0
                    for buf in f_iter:  # 使用生成的文件迭代器发送文件数据
                        sk.sendall(buf)
                        num+=1
                        print(num)
                elif sign[0] == "get_img":
                    f_iter = menu[sign[0]](data)
                    num = 0
                    for buf in f_iter:  # 使用生成的文件迭代器发送文件数据
                        sk.sendall(buf)
                        num += 1
                        print(num)
                elif sign[0] == "file_uploading" :
                    ret = json.dumps("finish")
                    sk.sendall(bytes(ret, encoding="utf-8"))
                else:
                    ret_data = menu[sign[0]](data)  # 发送回客户端的信息
                    print(ret_data)
                    get_data = json.dumps(ret_data)
                    get_data = bytes(get_data, encoding="utf-8")
                    sk.sendall(get_data)
                    if ret_data ==  "account_error" and  sign[0] == "sign_in" :    #登入错误、注册不管成功失败连接将直接断开，不会循环等待
                        return None
                    n=1
            except Exception  as ex:  # 用于判断用户端是否断开连接，断开则删除套接字
                    return None


sk1 = socket.socket()
sk1.bind(('192.168.1.239', 5555))
sk1.listen()
inputs.append(sk1)
outputs = []
message_dict = {}
data = ''
n = 0
while True:
    r_list, w_list, e_list = select.select(inputs,[],[])
    for sk in r_list:
        #新用户发来请求
        if sk is sk1:
            conn,adress = sk1.accept()
            inputs.append(conn)
        else:
            n = n+1
            t =Thread(group=None, target=fun, name=f"{n}",args=(sk,))
            inputs.remove(sk)
            t.start()



