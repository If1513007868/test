#递归
#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
# 阶乘： n的阶乘为n * (n-1) * (n-2) * ... * 1

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# if __name__ == "__main__":
#     print(factorial(5))

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         print(n)
#         return n * factorial(n-1)
#
#
# if __name__== "__main__":
#
#     print(factorial(5))

def test():
    return test()
if __name__ == "__main__":
    test()
