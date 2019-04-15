# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-24 13:41'


def radix_sort(array):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            bucket[num].append(array[i])
        array.clear()
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    print(array)


radix_sort([10, 8, 4, -1, 2, 6, 7, 3])
