# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-19 08:04'

import sqlite3

db = "/Users/chenming/PycharmProjects/python_example/test.db"
drp_tb_sql = "drop table if exists staff"
crt_tb_sql = """
create table if not exists staff(
id integer primary key autoincrement unique not null,
name varchar(100),
city varchar(100)
);
"""
# 连接数据库
con = sqlite3.connect(db)
cur = con.cursor()
# 创建表
cur.execute(drp_tb_sql)
cur.execute(crt_tb_sql)
# 插入记录
insert_sql = "insert into staff (name, city) values (?, ?)"
cur.execute(insert_sql, ('Tom', 'New York'))
cur.execute(insert_sql, ('Kate', 'Chicago'))
cur.execute(insert_sql, ('Frank', 'Los Angels'))
con.commit()
# 查询记录
select_sql = "select * from staff"
cur.execute(select_sql)
# 返回一个list，list中的对象类型为tuple
date_set = cur.fetchall()
for row in date_set:
    print(row)

cur.close()
con.close()
