import threading
import time

#线程是中轻量级的进程，所有线程均在同一个进程中，共享全局内存，用于任务并行

#使用with 加锁
count = 0

def adder(addlock):
    global count
    with addlock:
        count = count + 1
        print(count)
        time.sleep(0.5)
        count = count + 1
        print(count)
addlock = threading.Lock()

threads = []
for i in range(10):
    thread = threading.Thread(target=adder,args=(addlock,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(count)




