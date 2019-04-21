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


# init and new
# __init__函数并不是真正意义上的构造函数，__init__方法做的事情是在对象创建好之后初始化变量。实例方法。
# __new__方法用于创建对象并返回对象，当返回对象时会自动调用__init__方法进行初始化。静态方法。
class Person(object):
    def __new__(cls, *args, **kwargs):
        print("in __new__")
        instance = object.__new__(cls)
        return instance

    def __init__(self, name, age):
        print("in __init__")
        self._name = name
        self._age = age


p = Person("wang", 33)
