#1.递归
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
# 阶乘： n的阶乘为n * (n-1) * (n-2) * ... * 1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


# if __name__ == "__main__":
#     print(factorial(5))
#使用递归函数优点是逻辑清晰简单，缺点是过深调用会导致栈溢出
# def test():
#     return test()
# if __name__ == "__main__":
#     print(test())

#x的n次幂 等于x 的n-1次幂乘x，x的0次幂等于1

def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)

#2.装饰器
#装饰器是可以调用的对象，其参数是另一个函数（被装饰的函数），装饰器可以处理
#被装饰的函数，然后把他返回，也可以将其替成另一个函数或调用对象

def deco(funnc):
    def inner():
        print("running inner()")
    return inner
@deco
def target():
    print("running target()")
@deco
def tae():
    print("runner")

if __name__ == "__main__":
    print(factorial(5))
    print(power(2,6))
    target()
    tae()



