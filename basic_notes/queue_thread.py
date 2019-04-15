# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-24 15:09'

import queue
import threading
import time

exitFlag = 0


class MyThread (threading.Thread):
    # 创建线程并实例化
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.q = q

    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)


def process_data(thread_name, q):
    while not exitFlag:
        # 获取锁，用于线程同步
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (thread_name, data))
        else:
            # 释放锁，开启下一个线程
            queueLock.release()
        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = MyThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
