#可迭代的对象，迭代器
#迭代的意思是重复做一些事很多次，for循环
# 就是一种迭代，列表，字典，元组都是可迭代对象
# 实现__iter__方法的对象都是可迭代的对象。
# iter 返回一个迭代器，所谓迭代器就是具有next方法的对象
# 在掉用next方法的时，迭代器会返回它的下一个值，如果没有值了，则返回StopIteration

# b = [1,2,3]
# c = b.__iter__()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
#使用类定义迭代器，斐波那契数
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a,self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self
fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

#生成器
#生成器函数 生成器是一种用函数语法定义的迭代器;
# 调用生成器函数返回一个迭代器 yield语句挂起生成器函数并向调用者发送一个值
# ，迭代器的_next__继续运行函数
L = [[1,2],[3,4],[5,6]]
def flat(L):
    for sublist in L:
        for e in sublist:
            yield e
for num in flat(L):
    print(num)

#生成器send方法
#生成器函数执行到yield 时就会暂停，执行send收继续运行到下一次循环yield时再暂停，send的值付给x
def gen():
    for i in range(10):
        x = (yield i)
        print(x)

g = gen()
next(g)
print(g.send(11))
print(g.send(22))


