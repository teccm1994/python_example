# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-24 14:59'

import threading
import time

exit_flag = 0


class MyThread(threading.Thread):
    # 创建线程并实例化
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    # 表示线程活动的方法
    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if exit_flag:
            thread_name.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)


# 启动线程活动
thread1.start()
thread2.start()
# 等待至线程中止
thread1.join()
thread2.join()
print("退出主线程")
