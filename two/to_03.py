# os 和os.path
# 1.os 模块
# 返回当前目录 os.getcwd()
# 列出目录的内容 os.listdir()
# 创建目录 os.mkdir("te")
# 删除空目录 os.rmdir("te")
# 重命名 os.rename('1.py','2.py')
# 删除文件 os.remove('2.py')
# 执行系统命令 os.system("dir")
# 退出程序 os._exit(0)
# 遍历目录中的所有文件 os.walk 返回一个3元组生成器 当前目录的名称，当前目录中子目录的列表，当前目录中文件的列表

import os,sys
# 返回当前目录 os.getcwd()
os.chdir("E:\py\python\phone" )        # 切换到 "/var/www/html" 目录
print("当前目录为:%s"% os.getcwd())      # 打印当前目录



