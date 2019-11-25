#线程进程
from random import randint
from time import time,sleep
from threading import Thread
#
# class DownloadTask(Thread):
#
#     def __init__(self, filename):
#         super().__init__()
#         self._filename = filename
# def download_task(filename):
#     print('开始下载%s...' % filename)
#     time_to_download =randint(1,4)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
# def main():
#     start = time()
#     t1 = Thread(target=download_task,args=('Python从入门到住院.pdf',))
#     t1.start()
#     t2 =Thread(target=download_task,args=('Peking Hot.avi',))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('耗时%d秒'%(end-start))
#     # start = time()
#     # download_task('Python从入门到住院.pdf')
#     # download_task('Peking Hot.avi')
#     # end =time()
#     # print('耗时%d秒'%(end-start))
#
#
# if __name__ == '__main__':
#     main()

from time import sleep
from threading import Thread


class Account(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        # 计算存款后的余额
        new_balance = self._balance + money
        # 模拟受理存款业务需要0.01秒的时间
        sleep(0.01)
        # 修改账户余额
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()