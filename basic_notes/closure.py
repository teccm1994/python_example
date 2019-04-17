# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-24 14:40'


# 定义一个函数
def plus(number):
    # 在函数内部定义一个函数，该函数即闭包
    def plus_in(num_in):
        print(num_in)
        return num_in + number
    # 返回闭包的结果
    print(plus_in(100))


plus(20)


def mulby(num):
    print('num:', num)

    def gn(val):
        return num * val
    return gn


zw = mulby(7)
print(zw(9))



