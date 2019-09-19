import threading
import time

# def hell_oword():
#     time.sleep(2)
#     print("helloword")
#
# t = threading.Thread(target=hell_oword)
# t.start()
# print("main thread")
# #实例2 同种任务并行
# def helloworld(id):
#     time.sleep(2)
#     print("thread %d helloworld" % id)
#
#
# for i in range(5):
#     t = threading.Thread(target=helloworld, args=(i,))
#     t.start()
# print("main thread")

#实例3 线程间同步
count = 0
def adder():
    global count
    count += 1
    time.sleep(0.5)
    count += 1
threads = []
for i in range(2):
    thread = threading.Thread(target=adder)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print(count)



