# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-26 08:29'

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程：" + self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("退出主线程")
