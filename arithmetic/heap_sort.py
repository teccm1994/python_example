# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-24 13:18'


def heap_sort(array):
    def heap_adjust(parent):
        # left child
        child = 2 * parent + 1
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child+1] > heap[child]:
                    child += 1
            if heap[parent] >= heap[child]:
                break
            heap[parent], heap[child] = heap[child], heap[parent]
            parent, child = child, 2*child+1

    heap, array = array.copy(), []
    # 从2开始，到-1结束，增量为-1
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)
        print("%s time: %s" % (i, heap))
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        array.insert(0, heap.pop())
        heap_adjust(0)
    print(array)


heap_sort([10, 8, 4, -1, 2, 6, 7, 3])

