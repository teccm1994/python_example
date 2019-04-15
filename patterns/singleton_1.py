# -*- coding:utf-8 -*-
__author__ = 'chen_ming'
__date__ = '2019-03-21 20:48'


class Singleton(object):
    __instance = None

    # 不能使用__init__，这是在instance已经生成后调用的
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(
                Singleton, cls).__new__(cls)
        return cls.__instance

    def __init__(self, status_number):
        self.status_number = status_number


s1 = Singleton(2)
s2 = Singleton(5)
print(s1)
print(s2)

print(s1.status_number)
print(s2.status_number)
