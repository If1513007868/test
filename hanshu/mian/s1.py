# 面向对象
# 有意义的面向对象代码
#类下面的函数成为方法,   方法：面向对象设计层面，，函数：程序运行，过程式一种称谓

# 类 = 面向对象
# 类对象    通过类（模板）产生很多对象
#实例化
#类最基本的作用就是封装代码
#类只负责描述定义，不会执行代码，运行调用类要放到外部（另外模块）

#2.类和对象的关系   类：他将数据及这些数据上的操作封装在一起

class Student():
    name = 'nihao'        #数据成员，，每一个变量数据，刻画一些特征（行为）
    age = 0
    #类变量
   #行为与特征
    def __init__(self,name,age):   #构造函数 （可以让模板生产不同的对象） 1.函数调用自动进行

        self.name = name #实例变量          #初始化对象属性
        self.age = age
        #return None                         #对构造函数要求只能返回None


student1 = Student('你是',12)     #实例化，当类被实例化会变成个对象
student2 = Student('woshi ',15)
#student = Student()
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(Student.name)
print(student1.__dict__)
print(Student.__dict__)
# a = student.__init__()  #很少这样调用
# print(type(a))
