# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-04-17 22:31'

import dis
import timeit


# swap
def swap1():
    x = 5
    y = 6
    x, y = y, x


def swap2():
    x = 5
    y = 6
    tmp = x
    x = y
    y = tmp


# join vs plus
# join在连接字符串的时候，会先计算需要多大的内存存放结果，然后一次性申请所需内存并将字符串复制过去
# 操作符+连接字符串的时候，每执行一次+都会申请一块新的内存，然后复制上一个+操作的结果和本次操作的右操作符到这块内存空间，因此用+连接字符串的时候会涉及好几次内存申请和复制
def join_test(str_list):
    return "".join(str_list)


def plus_test(str_list):
    result = ""
    for v in str_list:
        result += v
    return result


# finally: 在finally中使用return会导致很多问题
def func1():
    try:
        print('in func1 try: try statement, will return 1')
        return 1
    finally:
        print('in func1 finally: try statement, will return 2')
        return 2


# try中抛出的异常是ValueError类型的，而except中定位的是IndexError类型的，try中抛出的异常没有被捕获到，所以except中的语句没有被执行，但不论异常有没有被捕获，finally还是会执行，最终函数返回了finally中的返回值3。
def func2():
    try:
        print('in func2 try: raise error')
        raise ValueError()
    except IndexError:
        print('in func2 except: caught error, will return 1')
        return 1
    finally:
        print('in func2 finally: will return 3')
        return 3


if __name__ == "__main__":
    # swap
    # print("swap1: ")
    # print(dis.dis(swap1))
    # print("swap2: ")
    # print(dis.dis(swap2))

    # join vs plus
    # str_list = ["a very very very very very very long string"]
    # timer1 = timeit.Timer("join_test(str_list)", "from __main__ import str_list, join_test")
    # timer2 = timeit.Timer("plus_test(str_list)", "from __main__ import str_list, plus_test")
    # time1 = timer1.timeit(number=100)
    # time2 = timer2.timeit(number=100)
    # print("join: %f, plus: %f" % (time1, time2))

    print(func1())
    print(func2())
