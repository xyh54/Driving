"""
@file:   1.py
@date:   2019/04/15
"""

import  time
class visitor(object):       #游客身份
    def __init__(self,inf):
        self.user = inf[0]
        self.pwd = inf[1]
        self.time = inf[2]
        self.identity = inf[3]
    #查看个人信息
    def look_account(self):
        return{"user":self.user,"time":self.time,"identity":self.identity}
    #查看老师，练车预约
    def appointment_time(self):
        pass
class student(visitor):        #学员身份
    def __init__(self,args):
        super().__init__(args)
        self.ID = args[4]
        self.name = args[5]
        self.address = args[6]
        self.life = args[7]
        self.phone = args[8]
        self.appointment_sign = 0
    def look_account(self):
        inf = {"ID":self.ID,"name":self.name,"address": self.address,"life":self.life,"phone":self.phone}
        inf.update(super(student,self).look_account())
        return inf
