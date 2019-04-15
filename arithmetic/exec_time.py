# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-24 13:52'

from _datetime import datetime


# 显示函数执行时间
def exectime(func):
    def inner(*args, **kwargs):
        begin = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        inter = end - begin
        print('E-time:{0}.{1}'.format(
            inter.seconds,
            inter.microseconds
        ))
        return result

    return inner
