import threading
import time

#线程是中轻量级的进程，所有线程均在同一个进程中，共享全局内存，用于任务并行
def helloword():
    time.sleep(2)
    print("第一次指定")

t = threading.Thread(target=helloword)
t.start()


print("zhiin")



