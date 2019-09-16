

class Student():
    sum = 0    #学生总数
    name = 'wang'
    age = 10

    #实例方法   对象和实例相关联，也是实例可以调用的方法
    def __init__(self,name,age):    #self默认传入
        self.name = name
        self.age = age
        #print(self.name)
        #print(self.__dict__)
        #print(age)  #读取的是形参的内容

        # print(Student.sum)
        # print(self.__class__.sum)#内部访问类变量
    def do_homework(self):
        print("xiezuoye ")


student1 = Student('你是',12)
#student1.do_homework()
#student2 = Student('woshi ',15)
print(student1.name,student1.age)
print(Student.sum)   #访问类变量

