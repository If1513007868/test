
#类方法
class Student():
    sum = 0    #学生总数
    # name = 'wang'
    # age = 10

    #实例方法   对象和实例相关联，也是实例可以调用的方法
    def __init__(self,name,age):    #self默认传入
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print('班级人数总数' + str(self.__class__.sum))  #为什么要加str



    def do_homework(self):   #实例关联的是对象
        self.__class__.sum += 1
        # print('班级人数总数' + str(self.__class__.sum))
        # print('name')

        #如何定义一个类方法
    @classmethod   #类与实例方法的区别，增加  @classmethod
    def pl_sum(cls):
        cls.sum += 1   #关联的是类本身
        print(cls.sum)

    @staticmethod  #静态方法     不要经常使用！！！！！！
    def add(x,y):
        print("这是一个静态方法")
        print(Student.sum)       #内部也可以访问类变量

#在类和静态中引用实例变量会报错

student1 = Student('你是',12)
#用一个对象调用类的方法？可以不要这做#student1.pl_sum()
student1.add(1,2)    #实例方法调用静态
Student.add(2,3)        #类方法调用静态

# #student1.do_homework()
# student2 = Student('你是1',12)
# Student.pl_sum()
# student3 = Student('你是2',12)
# Student.pl_sum()
# student4 = Student('你是3',12)


