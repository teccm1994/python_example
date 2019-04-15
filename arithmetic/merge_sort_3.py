# -*- coding:utf-8 -*-
# 二路归并排序：假设初始表含有n个记录，将其看成n个有序的子表，每个子表的长度为1，两两归并，得到n/2个长度为2或1的有序子表，再两两归并，依次重复，直到得到一个长度为n的有序子表为止。
__author__ = 'chen_ming'
__date__ = '2019-03-21 22:24'


def merge_sort(array):
    def merge_arr(arr_l, arr_r):
        array = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] <= arr_r[0]:
                array.append(arr_l.pop(0))
            elif arr_l[0] > arr_r[0]:
                array.append(arr_r.pop(0))
        if len(arr_l) != 0:
            array += arr_l
        elif len(arr_r) != 0:
            array += arr_r
        return array

    def recursive(array):
        if len(array) == 1:
            return array
        # 取整除 - 向下取接近除数的整数
        mid = len(array) // 2
        arr_l = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return merge_arr(arr_l, arr_r)

    print(recursive(array))


merge_sort([10, 8, 4, -1, 2, 6, 7, 3])
