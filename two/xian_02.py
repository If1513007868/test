# import threading,time
#
# #使用with 加锁
#
# count = 0
#
# def adder(addlock):
#     global count
#     with addlock:
#         count = count + 1
#     time.sleep(0.1)
#     with addlock:
#         count = count + 1
#
# addlock = threading.Lock()  #为什么加括号
# threads = []
# for i in range(100):
#     thread = threading.Thread(target=adder,args=(addlock,))
#     thread.start()
#     threads.append(thread)
# for thread in threads:
#     thread.join()
# print(count)



