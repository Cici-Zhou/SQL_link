#-*- coding:utf-8 -*-
from os import getenv
import pymssql
import re

server = '192.168.0.63'
user = 'sa'
password = 'qwe123!@#'
# execute(self, query, args):执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
# n=cursor.executemany(sql,param)
# 需要注意的是(或者说是我感到奇怪的是),在执行完插入或删除或修改操作后,需要调用一下conn.commit()方法进行提交.这样,数据才会真正保 存在数据库中.我不清楚是否是我的mysql设置问题,
# 总之,今天我在一开始使用的时候,如果不用commit,那数据就不会保留在数据库中,但是,数据 确实在数据库呆过.因为自动编号进行了累积,而且返回的受影响的行数并不为0.

def operation_table(con2, con3, con4, *args):
    # *args中显示需要显示的字段信息
    l = len(args)
    arg = args[0]
    for i in range(1,l):        
        arg2 = args[i]
        arg = arg +','+ arg2
    print(arg)

    cursor.execute("SELECT %s FROM staff_table where %s %s %s " % (arg, con2, con3, con4))
    
def search_by_dept(con):
    cursor.execute('SELECT * FROM staff_table where dept = %s', con)

def del_by_id(con):
    cursor.execute('DELETE FROM staff_table where id = %d', con)

def update_by_dept(con1, con2):
    cursor.execute('UPDATE staff_table set dept=%s WHERE dept= %s', con1, con2)

with pymssql.connect(server, user, password, "TEST1") as conn:
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute("""
        IF OBJECT_ID('staff_table', 'U') IS NOT NULL
        DROP TABLE staff_table
        CREATE TABLE staff_table(
            staff_id int IDENTITY(1,1),
            name varchar(20),
            age SMALLINT,
            phone varchar(11) PRIMARY KEY,
            dept varchar(10),
            enroll_date DATE
            )
        """)
        #插入多行数据
        cursor.executemany(
            "INSERT INTO staff_table VALUES (%s, %d, %d, %s, %s)",
            [('Alex Li', 22, 13651054608, 'IT', '2013-04-01'),
             ('Jack Wang', 30, 13304320533, 'HR', '2015-05-03'),
             ('Rain Liu', 25, 1383235322, 'Sales', '2016-04-22'),
             ('Mack Cao', 40, 1356145343, 'HR', '2009-03-01')])
            # 你必须调用 commit() 来保持你数据的提交(如果你没有将自动提交设置为true)
        conn.commit()
        con1 = 'name'
        con2 = 'age'
        con3 = '>'
        con4 = '22'

        operation_table(con2, con3, con4,'name','age','phone')
        for row in cursor:
            print('row = %r' %(row,))


# 遍历数据（存放到元组中）方式
# row = cursor.fetchone()
# while row:
#     print("ID=%d, Name=%s" % (row[0], row[1]))
#     row = cursor.fetchone()
# 遍历数据（存放在元组中） 方式2


# 遍历数据（存放在字典中）
# cursor = conn.cursor(as_dict=True)
# cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
# for row in cursor:
#     print("ID=%d, Name=%s" % (row['id'], row['name']))


# with pymssql.connect(host, database,user, password) as conn:
#    with conn.cursor(as_dict=True) as cursor: # 数据存放到字典中
#        cursor.execute("""CREATE PROCEDURE FindPerson @name VARCHAR(100) AS DEBUG SELECT * FROM Persons WHERE name = @name END """)
#        cursor.callproc('FindPerson', ('Jane Doe',))
#        for row in cursor:
#            print("ID=%d, Name=%s" %(row['id'], row['name']))
            

