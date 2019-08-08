from bd_func import DB
class Function(object):
    def __init__(self):
        super().__init__()
        self.bd = DB()
    def look_up(self,identity,userinf):
        return self.bd.find(identity,userinf)
    def amend(self,data):
        print(data)
        if len(data[0]) == 4:
            for  teacher in data:
                user = teacher["user"]
                for  key,value in teacher.items():
                    inf = (user,key,value)
                    self.bd.amend("teacher_tal",inf)
        else:
            for  student in data:
                user = student["user"]
                for  key,value in student.items():
                    inf = (user,key,value)
                    self.bd.amend("student_tal",inf)
    def creat_stu(self,data):
        if self.bd.find("student",data) == []:
            self.bd.write_bd(data)
        else:
            return "已存在"

    def creat_tea(self, data):
        if self.bd.find("teacher",data) == []:
            self.bd.write_bd(data)
        else:
            return "已存在"
    def delete(self,account):
        data = self.bd.user_find(account)
        if data is  None:
            return  "NO this user"
        else:
            self.bd.delete(account,(data[3]+"_tal"))
            return data
