# 多进程模块
# multiprocessing 模块

import os
from multiprocessing import Process, Lock
# def whoami(label, lock):
#     msg = '%s: name:%s, pid:%s'
#     with lock:
#         print(msg % (label, __name__,os.getpid()))
#
# if __name__ == '__main__':
#     lock = Lock()
#
#     for i in range(5):
#         p = Process(target=whoami, args=('child', lock))
#         p.start()

#进程池
from multiprocessing import Pool
import time


def func(num):
    print("hello world %d" % num)
    time.sleep(3)


if __name__ == '__main__':

    pool = Pool(processes=4)

    for i in range(100):
        pool.apply_async(func, (i,))
    pool.close()
    pool.join()
