# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-19 08:21'

import pymysql

con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='test_mysql')
cur = con.cursor()

sql_1 = cur.execute("update hosts set host = '1.1.1.2'")
sql_2 = cur.executemany("insert into hosts(host, color_id) values (%s, %s)", [("1.0.0.1", 1), ("10.0.0.3", 2)])

new_id = cur.lastrowid
cur.execute("select * from hosts")

row_1 = cur.fetchone()
print(row_1)
row_2 = cur.fetchmany()
print(row_2)
row_3 = cur.fetchall()
print(row_3)
cur = con.cursor(cursor=pymysql.cursors.DictCursor)
con.commit()

cur.close()
con.close()

