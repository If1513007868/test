print('1.----------------------函数---------------------------------------')
print('----------------------函数的参数---------------------------------------')
print('''。在Python中，函数的参数可以有默认值，
也支持使用可变参数，所以Python并不需要像其他语言一样支持函数的重载，
因为我们在定义一个函数的时候可以让它有多种不同的使用方式，''')
from random import randint
def roll_dice(n=2):
    """摇骰子"""
    totle = 0
    for i in range(n):
        totle += randint(1,6)
    return totle

def add(a=0,b=0,c=0):
    """三个数相加"""
    return a+b+c

print(roll_dice())
print(roll_dice(3))

print(add())
print(add(1,2,4))

print('----------------------在参数名前面的*表示args是一个可变参数---------------------------------------')
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
print(add(1,2,3,4))

print('''
最简单的场景就是在同一个.py文件中定义了两个同名函数，
由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，
也就意味着两个函数同名函数实际上只有一个是存在的''')
# def foo():
#     print('hello, world!')
#
# def foo():
#     print('goodbye, world!')
# # 下面的代码会输出什么呢？
# foo()
