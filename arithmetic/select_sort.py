# -*- coding:utf-8 -*-
# 直接选择排序：每一趟在待排序的记录中选出关键字最小的记录，依次放在已排序的记录序列的最后，直到全部记录排完为止。
__author__ = 'chen_ming'
__date__ = '2019-03-24 10:58'


def select_sort(array):
    count = len(array)
    for i in range(0, count):
        min = i
        for j in range(i+1, count):
            if array[min] > array[j]:
                min = j
        array[min], array[i] = array[i], array[min]
    print(array)


select_sort([10, 8, 4, -1, 2, 6, 7, 3])
