import sys

#基础
#一、迭代器
# 1.迭代是Python最强大的功能之一，是访问集合元素的一种方式
# 2.迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退
# 3.迭代器有两个基本的方法：iter() 和 next()

#1>迭代器对象可以使用常规for语句进行遍历：
list = [1,2,3,4,5]
it = iter(list)  # 创建迭代器对象
for x in it:
    print(x)
print("---------------------")
#2>也可以使用next()函数：
list = [1,2,3,4,5]
it = iter(list)   # 创建迭代器对象

# while True:
#     try:
#         print(next(it))
#     except StopIteration:   #异常用于标识迭代的完成，防止出现无限循环的情况
#         sys.exit()

# 二.生成器
# 1.使用了 yield 的函数被称为生成器（generator）
# 2.跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值,
# 3.并在下一次执行 next() 方法时从当前位置继续运行
# 4.调用一个生成器函数，返回的是一个迭代器对象
#1> yield 实现斐波那契数列

def fibonacci(n):

    a, b, counter = 1, 0, 1
    while True:
        if counter > n:
            return
        yield a
        a, b =b , a+b
        counter += 1

f = fibonacci(5)  # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()

# 三错误和异常
#Python 的查找顺序为：局部的命名空间去 -> 全局命名空间 -> 内置命名空间
# 语法错误  SyntaxError: invalid syntax
# 异常    TypeError:


