import threading, time

count = 0
#不加锁会出现执行几次后出现不一样的结果
def adder():
    global count
    count = count + 1
    time.sleep(0.5)
    count = count + 1

threads = []
for i in range(136):
    thread = threading.Thread(target=adder)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(count)

# count = 0
#
# def adder(addlock):
#     global count
#     addlock.acquire()
#     count = count + 1
#     addlock.release()
#     time.sleep(0.1)
#     addlock.acquire()
#     count = count + 1
#     addlock.release()   #加锁一定要及得释放锁，否则会不释放拿不到资源，程序卡死
#
# addlock = threading.Lock()
# threads = []
# for i in range(10):
#     thread = threading.Thread(target=adder,args=(addlock,))
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()

# print(count)

#用with加锁，会自动释放
count = 0

def adder(addlock):
    global count
    with addlock:
        count = count + 1
    time.sleep(0.1)
    with addlock:
        count = count + 1

addlock = threading.Lock()
threads = []
for i in range(100):
    thread = threading.Thread(target=adder,args=(addlock,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(count)