"""
@file:   mysqlsever.py
@date:   2019/04/16
"""
import random
import mysql.connector
DB_INF = {
    "user":'root',
    "password":'rootroot',
    "host":'localhost',
    "port":'3306',
    "database":'driving_school',
}
class DB (object):
    def __init__(self):
        self.db_inf = DB_INF

    def write_bd(self, kwargs):  # 增
        print("stu", kwargs)
        conn = mysql.connector.connect(
            user=self.db_inf["user"],
            password=self.db_inf["password"],
            host=self.db_inf['host'],
            port=self.db_inf['port'],
            database=self.db_inf["database"]
        )
        sql_data = ''
        cursor = conn.cursor()

        if kwargs['identity'] == "visitor":

            sql_data = f"INSERT INTO VISITOR_TAL(USER ,\
                                 PASSWORD,CREATE_DATE ,IDENTITY)\
                                  VALUES('{kwargs['user']}','{kwargs['password']}','{kwargs['create_date']}','{kwargs['identity']}')"
            cursor.execute(sql_data)
            conn.commit()
            return kwargs
        elif kwargs["identity"] == "student":
            sql_data = "INSERT INTO STUDENT_TAL(USER ,\
                              PASSWORD,CREATE_DATE ,IDENTITY,\
                              ID,NAME,ADDRESS,LIFE,PHONE)\
                              VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                       (kwargs["user"], kwargs["password"], kwargs["date"], kwargs["identity"], \
                        kwargs["ID"], kwargs["name"], kwargs["address"], kwargs["life"], kwargs["phone"])
            cursor.execute(sql_data)
            conn.commit()
            return kwargs
        else:
            sql_data = f"INSERT INTO TEACHER_TAL(USER\
                                            PASSWORD,NAME ,IDENTITY,PHONE,IMG)\
                                             VALUES('{kwargs['user']}',{kwargs['password']}','{kwargs['name']}','{kwargs['identity']}','{kwargs['phone']}','{kwargs['img']}')"

            cursor.execute(sql_data)
            conn.commit()
            data = self.find(kwargs['user'])
            sql_data = f"INSERT INTO APPOINTMENT(ID VALUES('{data[0]}'))"
            return kwargs

    def find(self,account):         #查
        print("开头1")
        conn = mysql.connector.connect(
            user=self.db_inf["user"],
            password=self.db_inf["password"],
            host=self.db_inf['host'],
            port=self.db_inf['port'],
            database=self.db_inf["database"]
        )
        cursor = conn.cursor()
        sql_data1 = f"SELECT *  FROM visitor_tal   WHERE BINARY user='{account}'"
        sql_data2 = f"SELECT *  FROM student_tal   WHERE BINARY user='{account}'"
        sql_data3 = f"SELECT *  FROM teacher_tal,appointment  WHERE BINARY user='{account}' AND id = apptal_id"

        cursor.execute(sql_data1)
        results = cursor.fetchall()
        print(results)
        if results == []:
            print("的二次")
            cursor.execute(sql_data2)
            results = cursor.fetchall()
            print(results)
            if  results == []:
                print("第3次")
                cursor.execute(sql_data3)
                results = cursor.fetchall()
        if  results != [] :
            li = list(results[0])
            return li
        else:
            return None
    def delete(self,user,tal_name):     #删
        print(user,tal_name)
        conn = mysql.connector.connect(
            user=self.db_inf["user"],
            password=self.db_inf["password"],
            host=self.db_inf['host'],
            port=self.db_inf['port'],
            database=self.db_inf["database"]
        )
        cursor = conn.cursor()
        sql_data = f"SELECT *  FROM {tal_name} WHERE BINARY user= '{user}'"
        cursor.execute(sql_data)
        print("qwe")
        results = cursor.fetchall()
        print("sss")
        print(results)
        if results == []:
            return None
        else:
            cursor.execute(f"DELETE FROM {tal_name} WHERE  user='{user}';")
            conn.commit()
            return results
    def amend(self,tal_name,am_inf):  #改
        conn = mysql.connector.connect(
            user=self.db_inf["user"],
            password=self.db_inf["password"],
            host=self.db_inf['host'],
            port=self.db_inf['port'],
            database=self.db_inf["database"]
        )
        cursor = conn.cursor()
        sql_data = f"SELECT *  FROM {tal_name} WHERE BINARY user='{am_inf[0]}'"
        cursor.execute(sql_data)
        results = cursor.fetchall()
        if results == []:
            return None
        else:
            cursor.execute(f"SELECT * FROM information_schema.COLUMNS where TABLE_NAME = '{tal_name}'")
            results = cursor.fetchall()
            for  field in results:
                if field == am_inf[1]:
                    break
            else:
                return None
            cursor.execute(f"UPDATE {tal_name} SET {am_inf[1]} = '{am_inf[2]}' WHERE user = '{am_inf[0]}'")
            conn.commit()
            return "OK"

    def input_all(self,tal_name):   #输出表中所有数据
        conn = mysql.connector.connect(
            user=self.db_inf["user"],
            password=self.db_inf["password"],
            host=self.db_inf['host'],
            port=self.db_inf['port'],
            database=self.db_inf["database"]
        )
        cursor = conn.cursor()
        if tal_name == "teacher_tal":
            sql_data = f"SELECT * FROM teacher_tal,appointment WHERE id = apptal_id"
        else:
            sql_data = f"SELECT  *  FROM  {tal_name}"
        cursor.execute(sql_data)
        results = cursor.fetchall()
        return results
    def  add_app_stu(self,data):
        conn = mysql.connector.connect(
            user=self.db_inf["user"],
            password=self.db_inf["password"],
            host=self.db_inf['host'],
            port=self.db_inf['port'],
            database=self.db_inf["database"]
        )
        cursor = conn.cursor()
        cursor.execute(f"UPDATE appointment SET {data[0]} = '{data[1]}' WHERE id = '{data[2]}'")
        conn.commit()
        return "finish"
    def test(self,num):
        print("test")
        conn = mysql.connector.connect(
            user=self.db_inf["user"],
            password=self.db_inf["password"],
            host=self.db_inf['host'],
            port=self.db_inf['port'],
            database=self.db_inf["database"]
        )
        li = []
        data = []
        cursor = conn.cursor()
        while True:
            i = random.randint(1,100)
            print(1)
            if  i not in li:
                li.append(i)
            if len(li)>=num:
                break
        print(li)
        for i  in li:
            # f"SELECT *  FROM visitor_tal   WHERE BINARY user='{account}'

            cursor.execute(f"SELECT *  FROM questions_bank WHERE BINARY id={i}")
            results = cursor.fetchall()
            data.append(results[0])
        print(data)
        return data



