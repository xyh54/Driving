"""
@file:   soketway.py
@date:   2019/04/15
"""
import socket
import select
import sys
import time
import json
class SocketException(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg
class client_soket(object):
    def __init__(self):
        self.url  = "192.168.43.209"
        self.port = 5555
        self.obj = socket.socket()
        self.obj.settimeout(10)  # 设置超时
        self.obj.connect((self.url, self.port))
    def receive(self):
        start = time.time()
        data =self.obj.recv(1024)
        spent = time.time() - start
        if spent > 10:
            raise SocketException("连接超时")
        data.decode("utf-8")
        data = json.loads(data)
        return data
    def send(self,data):
        data = json.dumps(data)
        data = bytes(data, encoding="utf-8")
        start = time.time()
        self.obj.send(data)
        spent = time.time() - start
        if spent > 10:
            raise  SocketException("连接超时")
        return True
    def send_byte(self, data):
        start = time.time()
        self.obj.send(data)
        spent = time.time() - start
        if spent > 10:
            raise SocketException("连接超时")
        return True
    def receive_byte(self):
        start = time.time()
        data =self.obj.recv(1024)
        spent = time.time() - start
        if spent > 10:
            raise SocketException("连接超时")
        return data


