# -*- coding:utf-8 -*-
# 直接插入排序：每次将一个待排序的记录，按其关键字大小插入到前面已经排好序的子文件中的合适位置，直到全部记录插入完成为止。稳定排序算法。
__author__ = 'chen_ming'
__date__ = '2019-03-22 08:23'


# wrong
def insert_sort_1(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
            break
    print(array)


# 默认第一个元素是有序的，从第二个元素开始，每次将第i个元素设为key（哨兵），依次将i-1个元素之前的元素与key做比较，保证第i个元素前的区间元素是有序的。
def insert_sort_2(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
                print("%s-%s time: %s" % (i, j, lists))
            j -= 1
    print(lists)


insert_sort_2([10, 8, 4, -1, 2, 6, 7, 3])
