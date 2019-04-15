# -*- coding:utf-8 -*-
# PyMongo - the Python driver for MongoDB http://api.mongodb.org/python
# https://github.com/mongodb/mongo-python-driver
__author__ = 'chen_ming'
__date__ = '2019-03-19 21:31'


import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.test
print(db.name)

con = db.my_collection
con.insert_one({"x": 10}).inserted_id
res = con.find_one()
for item in res:
    print(item["x"])

