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

print("-----------返回当前目录 os.getcwd()--------------------")
print ("当前工作目录01 : %s" % os.getcwd())   # 打印当前目录
# 返回当前目录 os.getcwd()
os.chdir("/Users/mac/Desktop/123" )        # 切换到 "/var/www/html" 目录
print("当前目录为:%s"% os.getcwd())      # 打印当前目录
fd = os.open( "/Users/mac/Desktop/123", os.O_RDONLY )  # 打开 "/tmp"
os.fchdir(fd)  # 使用 os.fchdir() 方法修改目录
print ("当前工作目录 : %s" % os.getcwd())
os.close( fd )    # 关闭文件
print("   ")
print("-------------列出目录的内容 os.listdir()------------------")
# 打开文件
path = "/Users/mac/Desktop/123"
dirs = os.listdir(path)
# 输出所有文件和文件夹
for file in dirs:
    print(file)
print("   ")
print("-------------创建目录 os.mkdir("")------------------")
#os.mkdir() 方法用于以数字权限模式创建目录。默认的模式为 0777 (八进制)。
#mkdir()方法语法格式如下：os.mkdir(path[, mode])
#os.mkdir(path[, mode])    path -- 要创建的目录   mode -- 要为目录设置的权限数字模式




