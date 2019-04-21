# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-11 07:53'


# 可变对象创建后可改变但地址不会改变；不可变对象创建后不能改变，若改变则会指向一个新的对象。
# list
# 针对列表（可变类型），修改列表的方法（insert，remove， sort）没有打印返回值，返回None
list = [66.25, 333, 333, 1, 1234.5]

list.append(333)

list.insert(2, -1)

list.index(333)

list.remove(1)

list.pop(2)

list.count(1)

list.sort()

list.reverse()

# 1.把列表当作堆栈使用,append把一个元素添加到 堆栈顶，不指定索引的pop把一个元素从堆栈顶释放。
stack = [3, 4, 5]
stack.append(6)
stack.pop()


# 2.把列表当队列使用，最先进入的元素最先释放，先进先出，这样列表的使用效率低。
# collections.deque，为在收尾两端快速插入和删除而设计。
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.popleft()
queue.popleft()
queue

# 3.列表推导式，从序列中创建列表
# x变量在循环完毕后仍存在
squares = []
for x in range(10):
    squares.append(x**2)
squares
# 等价于
squares = list(map(lambda x: x**2, range(10)))
# 等价于
squares = [x**2 for x in range(10)]
# 举个栗子
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

from math import pi
list = [str(round(pi, i)) for i in range(1, 6)]

# del从列表中按给定的索引而不是值来删除一个子项，或删除切片或清空整个列表。
a = [-1, 1, 66.25, 333, 333, 1234.5]
del(a[0])
del(a[2:4])
del(a[:])
del(a)

# 元组，由多个逗号分隔的值组成，不可变类型。通过分拆或索引访问
t = 12345, 54321, 'hello!'
v = ([1, 2, 3], [3, 2, 1])

empty = ()
singleton = 'hello'
single = 'hello',
len(empty)
len(singleton)
single
len(single)

# 集合，是一个无序不重复元素的集，用于挂你测试和消除重复元素。创建空集合必须使用set(),{}用于创建空字典
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
'orange' in basket

a = set('abracadabra')
b = set('alacazam')
a - b
a | b
a & b
a ^ b

c = {x for x in 'abracadabra' if x not in 'abc'}

# dict字典，以关键字为索引，关键字可以是任意不可变类型
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
del tel['sape']
list(tel.keys())
sorted(tel.keys())
'guido' in tel
'jack' not in tel
dict([('space', 2334), ('test', 4321), ('tom', 4089)])
dict(apse=2134, guido=3211, jck=2334)
{x: x**2 for x in (2, 4, 6)}

# 循环
# 字段循环同时取出键值对:items()
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 序列循环同时取出索引及对应值:enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时循环多个序列:zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

# 逆向循环: reversed()
for i in reversed(range(1, 10, 2)):
    print(i)

# 排序循环: sorted(),不改动原序列，生成一个新的已排序的序列
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# 在序列上循环不会隐式地创建副本，切片表示法
words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

# strip([chars]):去除头尾字符，空白符（\n, \r, \t, ' '）
# lstrip([chars]):去除开头字符，空白符
# rstrip([chars]):去除结尾字符，空白符
name = ' www.pythontab.com '
name.strip()
# 当chars不为空时，函数会被chars解成一个个的字符，然后将这些字符去掉。与顺序无关。
name = '-# www.pythontab.com #-'
name.strip('-#')

# 时间戳转换为指定格式的日期,datetime基于time进行封装，提供更多实用函数
import time
time_stamp = time.time()
time_array = time.localtime(time_stamp)
format_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
print(format_time)

import datetime
time_stamp = time.time()
time_array = datetime.datetime.utcfromtimestamp(time_stamp)
format_time = time_array.strftime("%Y-%m-%d %H:%M:%S")
print(format_time)

# 常用技巧
# 原地交换两个数字
x, y = 10, 20
y, x = x, y

# 链状比较
n = 10
print(1 < n < 20)
print(1 > n <= 9)

# 三元操作符实现条件赋值
y = 20
x = 9 if (y == 10) else 8

# 找abc最小的数
def small(a, b, c):
    return a if a<b and a<c else (b if b<a and b<c else c)
print(small(1,4,8))

# 多行字符串
multistr = "select * from multi_row \
where row_id < 5"
print(multistr)

# 列表元素存到新变量
list = [1, 2, 3]
x, y, z = list
print(x, y, z)

# 打印引入模块的绝对路径
import threading
import socket
print(threading)
print(socket)

# 调试脚本
import pdb
pdb.set_trace()

# 检车python中的对象
test = [1, 3, 5, 7]
print(dir(test))

# 运行时检查python版本
import sys
if not hasattr(sys, "hasversion") or sys.version_info != (2, 7):
    print("sorry, you are not running on python 2.7")
    print("current python version:", sys.version)

# 找列表中出现次数最多的数
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 4]
print(max(set(test), key=test.count))

# 一个对象的内存使用, python 3.5中一个32bit的整数占用28字节
import sys
x = 1
print(sys.getsizeof(x))


# 减少内存开支
import sys


class FileSystem(object):
    __slots__ = ['files', 'folders', 'devices']

    def __int__(self, files, folders, devices):
        self.files = files
        self.folder = folders
        self.devices = devices


print(sys.getsizeof(FileSystem))


# 获取对象信息
# 判断对象类型
type(123)
# 判断类的类型
isinstance('a', str)
# 获取一个对象所有的属性和方法
dir('ABC')

# is比较两个对象在内存中的地址是否一样,id(a) == id(b)
# ==检查两个对象是否相等,a.__eq__(b)
a = [1, 2, 3]
b = [1, 2, 3]
print('is: ', a is b)
print('==: ', a == b)


# None是单例对象，如果是None，一定和None指向同一个内存地址。
class Foo(object):
    def __eq__(self, other):
        return True


f = Foo()
print(f == None)
print(f is None)


# 字符串
def str_test(num):
    str = 'first'
    for i in range(num):
        str += 'X'
        return str


str = str_test(4)
print(str)

