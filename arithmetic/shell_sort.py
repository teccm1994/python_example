# -*- coding:utf-8 -*-
# 希尔排序：又称缩小增量排序。先取一个小于n的整数d1并作为第1个增量，将文件的全部记录分成d1个组，所有距离为d1倍数的记录放在同一个组，在各组内进行直接插入排序，然后取第2个增量d2（d2<d1），以此重复直到所取的增量d1=1为止，此时所有的记录放在同一组中进行直接插入排序。
__author__ = 'chen_ming'
__date__ = '2019-03-24 10:22'


def shell_sort(array):
    gap = len(array)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(array)):
            for j in range(i % gap, i, gap):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
    print(array)


shell_sort([10, 8, 4, -1, 2, 6, 7, 3])
