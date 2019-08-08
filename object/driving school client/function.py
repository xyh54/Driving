"""
@file:   function.py
@date:   2019/04/19
"""
import json
import time
import os
from client_soket   import client_soket
from account import visitor ,student
class SocketException(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg
VIDEO_DIR  =  "./video"
TEST_DIR = "./test"

class client(object):
    def __init__(self):
        self.cs  = client_soket()
    def enter(self,user,pwd):
        print("我")
        try:
            self.cs.send(("enter",0))
            data =self.cs.receive_byte()
        except SocketException as ret:
            return ret
        if data.decode("utf-8") != 'OK':
            return "连接失败"
        else:
            try:
                self.cs.send((user,pwd))
                data = self.cs.receive()
            except SocketException as ret:
                return ret
            if  data is None:
                return "不存在此用户"
            elif  data == "password_error":
                return "密码错误"
            else:
                if len(data)  == 4:
                    self.account = visitor(data)
                else:
                    self.account = student(data)
                return data
    def  promote_stu(self,inf):
        if isinstance(self.account,student):
            return "已经是了"
        else:
            try:
                self.cs.send(("promote_stu", 0))
                data = self.cs.receive_byte()
            except SocketException as ret:
                return ret
            if data.decode("utf-8") != 'OK':
                return "连接失败"
            else:
                try:
                    self.cs.send(inf)
                    data = self.cs.receive()
                except SocketException as ret:
                    return ret
                else:
                    if data is None:
                        return "失败"
                    else:
                        self.account =student(data)
    def sign_in(self,inf):
        date = time.strftime("%Y-%m-%d",time.localtime())
        print(date)
        inf["identity"] = "visitor"
        inf["create_date"] = date
        try:
            self.cs.send(("sign_in", 0))
            data = self.cs.receive_byte()
        except SocketException as ret:
            return ret
        if data.decode("utf-8") != 'OK':
            return "连接失败"
        else:
            try:
                self.cs.send((inf))
                data = self.cs.receive()
                print(data)
            except SocketException as ret:
                return ret
            print(inf)
            if data == "already_exist":
                return "用户已经存在"
            else:
                return "注册成功"

    def download_video(self,dir,filename):
        print("等待")
        download_size = 0
        try:
            self.cs.send(("file_download",0))
            data = self.cs.receive_byte()
        except SocketException as ret:
            return ret
        if data.decode("utf-8") != 'OK':
            return "连接失败"
        else:
            try:
                self.cs.send((filename))
                path = os.path.join(dir,filename)
                yield self.cs.receive()
                with open(path,'wb') as fp:
                    while True:
                        data = self.cs.receive_byte()
                        if len(data) <1024:
                            fp.write(data)
                            download_size = download_size + 1
                            return download_size
                        else:
                            fp.write(data)
                            download_size = download_size +1
                            yield download_size
            except SocketException as ret:
                return ret
    def all_teacher(self):
        try:
            self.cs.send(("get_all", 0))
            data = self.cs.receive_byte()
        except SocketException as ret:
            return ret
        if data.decode("utf-8") != 'OK':
            return "连接失败"
        else:
            try:
                self.cs.send("teacher_tal")
                data = self.cs.receive()
            except SocketException as ret:
                return ret
            else:
                return  data
    def test(self,num):
        try:
            self.cs.send(("test", 0))
            data = self.cs.receive_byte()
        except SocketException as ret:
            return ret
        if data.decode("utf-8") != 'OK':
            return "连接失败"
        else:
            try:
                self.cs.send(num)
                data = self.cs.receive()
            except SocketException as ret:
                return ret
            else:
                return  data
    def appointment_time(self,time,user,id):
        try:
            self.cs.send(("appointment_time", 0))
            data = self.cs.receive_byte()
        except SocketException as ret:
            return ret
        if data.decode("utf-8") != 'OK':
            return "连接失败"
        else:
            try:
                self.cs.send((time,user,id))
                data = self.cs.receive()
            except SocketException as ret:
                return ret
            else:
                return  data
    def get_video(self):
        try:
            self.cs.send(("cat_video", 0))
            data = self.cs.receive_byte()
        except SocketException as ret:
            return ret
        if data.decode("utf-8") != 'OK':
            return "连接失败"
        else:
            try:
                self.cs.send(self.account.identity)
                data = self.cs.receive()
            except SocketException as ret:
                return ret
            else:
                return data

    def get_img(self,img_name):
        print("等待")
        download_size = 0
        try:
            self.cs.send(("get_img", 0))
            data = self.cs.receive_byte()
        except SocketException as ret:
            return ret
        if data.decode("utf-8") != 'OK':
            return "连接失败"
        else:
            try:
                self.cs.send(img_name)
                path = os.path.join("img/", img_name)
                with open(path, 'wb') as fp:
                    while True:
                        data = self.cs.receive_byte()
                        if len(data) < 1024:
                            fp.write(data)
                            download_size = download_size + 1
                            return download_size
                        else:
                            fp.write(data)
                            download_size = download_size + 1
            except SocketException as ret:
                return ret

    def img_synchronization(self):
        for root, dirs, files in os.walk("img"):
            print(files)
            try:
                self.cs.send(("img_synchronization", 0))
                data = self.cs.receive_byte()
            except SocketException as ret:
                return ret
            if data.decode("utf-8") != 'OK':
                return "连接失败"
            else:
                try:
                    self.cs.send(files)
                    data = self.cs.receive()
                except SocketException as ret:
                    return ret
                for img_name in data:
                    self.get_img(img_name)
