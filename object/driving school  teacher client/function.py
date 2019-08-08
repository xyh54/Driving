"""
@file:   function.py
@date:   2019/04/19
"""
import json
import time
import os
from client_soket   import client_soket

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
        try:
            self.cs.send(("enter",0))
            data =self.cs.receive_byte()
            print(data)
        except SocketException as ret:
            return ret
        if data.decode("utf-8") != 'OK':
            return "连接失败"
        else:
            try:
                self.cs.send((user,pwd))
                data = self.cs.receive()
                print(data)
            except SocketException as ret:
                return ret
            if  data is None:
                return "不存在此用户"
            elif  data == "password_error":
                return "密码错误"
            else:
                self.account = data
                return data

    def cat_stu(self, user):
        try:
            self.cs.send(("cat_stu", 0))
            data = self.cs.receive_byte()
        except SocketException as ret:
            return ret
        if data.decode("utf-8") != 'OK':
            return "连接失败"
        else:
            try:
                self.cs.send(user)
                data = self.cs.receive()
                return data
            except SocketException as ret:
                return ret
    def video_uploading(self,path,filename):
        download_size = 0
        try:
            self.cs.send(("file_uploading", filename))
            data = self.cs.receive_byte()
        except SocketException as ret:
            return ret
        if data.decode("utf-8") != 'OK':
            return "连接失败"
        else:
            try:
                with open(path, 'rb') as fp:
                    while True:
                        data = fp.read(1024)
                        self.cs.send_byte(data)
                        download_size = download_size + 1
                        yield  download_size
                        if len(data) < 1024:
                            break
            except SocketException as ret:
                return ret
            return self.cs.receive()

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


