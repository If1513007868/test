
import os,sys
import threading
import time
# print(os.getcwd())  #当前目录
# print(os.listdir('d:/')
#       )   #\转义字符
# print("-------------------")
# #print(os.system("dir"))
# #print(os.popen('dir').read())
# # print(os._exit(1))
# # # print(3)
#
# for dirpath,dirames, filenames  in os.walk("E:\龙腾笔记"):
#     print('[' + dirpath + ']')
#     for filename in filenames:
#         print(os.path.join(dirpath,filename))

def helloworld():
    time.sleep(2)
    print("helloworld")
t = threading.Thread(target=helloworld)
t.start()
print("nihao ")
print("--------------")
def helloworld(id):
    time.sleep(2)
    print("thread %d helloworld" % id)


for i in range(5):
    t = threading.Thread(target=helloworld, args=(i,))
    t.start()
print("main thread")
