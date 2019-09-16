#
# def sum (a,b):
#     c = a+b
#     return c
#
# def code_a(code):
#     print(code)
#     return #函数遇到return就会终止，不会运行后面的语句
#     print(code_a())
#
# a = sum(1,2)
# b =code_a('python')
# print(a,b)

#2.多结果函数返回

def number(a,b): #形式参数，形参（a,b）
    number1 = a*3
    number2 = b*3+20
    return number1,number2
sun_1,sum_2 = number(a = 4,b = 5) #实际参数，实参（4，5）
                      #赋值参数，不需要考虑传入顺序

print(sun_1,sum_2)

#3333序列解包,,,元素个数要相等
#定义多少个形参就要传入多少个实参
# a = 1
# b = 2
# c = 3
#
# a,b,c = 1,2,3
# d= 1,2,3
# print(type(d))
# a,b,c = d

#3333函数参数
#1.必须参数（定义的参数必须要传参，如果其中一个不赋值，就会报错）
#2.关键字参数
#以上两者区别在于函数的调用，不在意函数的定义上
#3.默认参数   def number(a,5)

print('------------------------')
def auth():
    name = input(">>>:").strip()  #去除空格
    password = input(">>>:")
    if name == "test" and password == "123":
        print("登录成功")
    else:
        print("用户名密码错误")
auth()