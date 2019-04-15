# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-28 19:57'


# 生成器
def fib(max):
    """
    函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
    """
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


def fib_generator(max):
    """
    变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
    :return:
    """
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib_generator(6)
# for n in f:
#     print(n)

while True:
    try:
        x = next(f)
        print('f:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# function
def outer(func):
    def inner():
        print("我是内层函数！")
    return inner()


def foo():
    print("我是原始函数！")


outer(foo)
outer(foo())
