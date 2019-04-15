# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-18 08:19'

import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
print(r.get('foo'))
print(r.keys())
print(r.exists('hello'))
print(r.dbsize())
r['test'] = 'tester'
r.delete('foo')

# 清空数据库
r.flushdb()

