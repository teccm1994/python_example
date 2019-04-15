# -*- coding:utf-8 -*-
# 快速排序：分解-求解-组合。分治法的基本思想是将原问题分解成若干个规模更小但结构与原问题相似的子问题。递归地解决子问题，然后将子问题的解组合成原问题的解。
__author__ = 'chen_ming'
__date__ = '2019-03-24 11:11'


def quick_sort(array):
    def recursive(begin, end):
        if begin > end:
            return
        l, r = begin, end
        pivot = array[l]
        while l < r:
            while l < r and array[r] > pivot:
                r -= 1
            while l < r and array[l] <= pivot:
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = pivot, array[l]
        recursive(begin, l-1)
        recursive(r+1, end)

    recursive(0, len(array)-1)
    print(array)


quick_sort([10, 8, 4, -1, 2, 6, 7, 3])
