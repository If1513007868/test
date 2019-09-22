#def fect(n):
#     if n == 1:
#         return 1  #直接给出1的阶乘，先下后上（栈）
#     else:
#         return n * fect(n-1)
#
# if __name__ == "__main__":
#     print(fect(4))

#取出n层嵌套列表里的所有元素 提示判断一个元素i是否是list 使用isinstance(i,list)函数
# def face (a):        #可以用到取出文件夹下所有的文件
#     for i in a:
#         if isinstance(i,list):
#             face(i)  #face(item222)
#         else:
#             print(i,end=" ")  #end = ""  是默认不换行
#
#
# a = [1,2,3,[4,5,6]]
# face(a)


def deco(func):
    def inner():
        print("running inner()")
        func()
    return inner
#让被装饰的函数在不需要修改任何代码的时候有额外的功能
@deco
def target():
    print('running target()')

if __name__ == "__main__":
    #target = deco(target)
    target()
