"""
@file:   file_op.py
@date:   2019/04/17
"""
import os
import  sys
class FileOperation(object):
    def __init__(self):
        self.v_dir = "./video"
        self.t_dir = "./test"
        self.img_dir = "./img"
    def cat_video(self,identity):
        if identity != "student" and identity !="teacher":
            return  "permission denied"
        return os.listdir(self.v_dir)
    def cat_test(self):
        return os.listdir(self.t_dir)
    def file_download(self,filename):
        dir = os.path.join(self.v_dir, filename)
        BUF_SIZE = 1024
        with open(dir, "rb") as fp:
            while True:
                buf = fp.read(BUF_SIZE)
                if buf:
                    yield buf
                else:
                    return
    def test_download(self,filename):
        dir = os.path.join(self.t_dir, filename)
        BUF_SIZE = 1024
        with open(dir, "rb") as fp:
            while True:
                buf = fp.read(BUF_SIZE)
                if buf:
                    yield buf
                else:
                    return
    def file_uploading(self,filename,data):
        dir = os.path.join(self.v_dir, filename)
        BUF_SIZE = 1024
        with open(dir, "wb") as fp:
            num = 0
            while True:
                if data != "":
                    num = num + 1
                    fp.write(data)
                else:
                    return
                data = yield num

    def test_uploading(self,filename,data):
        print(filename)
        print(data)
        dir = os.path.join(self.t_dir, filename)
        with open(dir, "wb") as fp:
            num = 0
            while True:
                if data != "":
                    num = num + 1
                    fp.write(data)
                else:
                    return
                data = yield num
    def img_download(self,filename):
        print(filename)
        dir = os.path.join(self.img_dir, filename)
        BUF_SIZE = 1024
        with open(dir, "rb") as fp:
            while True:
                buf = fp.read(BUF_SIZE)
                if buf:
                    yield buf
                else:
                    return


