#面向对象

class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name,age)
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)
# 创建学生对象并指定姓名和年龄
stu1 = Student('骆昊', 38)
    # 给对象发study消息
stu1.study('Python程序设计')
    # 给对象发watch_av消息
stu1.watch_movie()
stu2 = Student('王大锤', 15)
stu1.study('Python程序设计')
stu2.watch_movie()

# class Test:
#
#     def __init__(self, foo):
#         self.__foo = foo
#
#     def __bar(self):
#         print(self.__foo)
#         print('__bar')
#
#
# def main():
#     test = Test('hello')
#     # AttributeError: 'Test' object has no attribute '__bar'
#     test.__bar()
#     # AttributeError: 'Test' object has no attribute '__foo'
#     print(test.__foo)
#
#
# if __name__ == "__main__":
#     main()

print('======================定义一个类描述数字时钟==========================')
from time import sleep


class Clock(object):
    """数字时钟"""
    def __init__(self,hour = 0,minute = 0,second = 0):
        """初始化方法

               :param hour: 时
               :param minute: 分
               :param second: 秒
               """
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        """走字"""
        self.second +=1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute =0
                self.hour +=1
                if self.hour == 24:
                    self.hour = 0
    def show(self):
        return ("%02d:%02d:%02d")\
            %(self.hour,self.minute,self.second)

clock = Clock(23, 59, 58)

while True:
        print(clock.show())
        sleep(1)
        clock.run()





