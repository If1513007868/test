import os

from multiprocessing import Process, Lock

def whoami(label, lock):
    msg = '%s: name:%s, pid:%s'
    with lock:
        print(msg % (label, __name__,os.getpid()))


if __name__ == '__main__':
    lock = Lock()

    for i in range(5):
        p = Process(target=whoami, args=('child', lock))
        p.start()