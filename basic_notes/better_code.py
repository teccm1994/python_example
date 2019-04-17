# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-04-17 22:31'

import dis
import timeit


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


if __name__ == "__main__":
    print("swap1: ")
    print(dis.dis(swap1))
    print("swap2: ")
    print(dis.dis(swap2))
