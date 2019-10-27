# -*- coding:utf-8 -*-
# 冒泡排序：将每个记录看做是重量为对应值的气泡，根据轻气泡不能在重气泡之下的原则，从下往上扫描数组，凡扫描到违反本原则的轻气泡就使其上浮，直到最后两个气泡都是轻者在上，重者在下。不稳定排序。
__author__ = 'chen_ming'
__date__ = '2019-03-24 10:43'


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                print(" the %s-%s time: %s" % (i, j, array))
    print(array)


bubble_sort([10, 8, 4, -1, 2, 6, 7, 3])
