#1.1-100求和
print('1、-----------------1-100求和--------------------------')
def sum():
    sum = 0
    for n in range(1, 101):
        sum = sum + n
    return sum


print(sum())
print('2、-----------------如何在一个函数内部修改全局变量--------global------------------')
# 2、如何在一个函数内部修改全局变量
a = 5
def fn():
    global a
    a = 4
fn()

print(a)
print('3、-----------------列出5个python标准库--------------------------')
print('os','time''re','sys','math','detatime')
print('4、-----------------字典如何删除键和合并两个字典-----update合并字典---------------------')
dic = {"name":"li","age":"18"}
del dic["name"]
print(dic)
dic2 = {"name":"tom"}
dic.update(dic2)
print(dic)

print('5、-----------------python实现列表去重的方法--------------------------')
list_01=[1,2,3,4,4,5,6,5,6,7]
a = set(list_01)
print(a)
print('-----------------集合去重--------------------------')
dic_01 = {11,2,23,2,23,4,5,}
for x in dic_01:
    print(x)

print('6、-----------------python2和python3的range（100）的区别--------------------------')
print('python2返回列表，python3返回迭代器，节约内存')
print('7、-----------------一句话解释什么样的语言能够用装饰器?--------------------------')
print('函数可以作为参数传递的语言，可以使用装饰器')
print('8、-----------------python内建数据类型有哪些--------------------------')
print('''整型--int
布尔型--bool
字符串--str
列表--list
元组--tupe
字典--dict''')

print('9、-----------------简述with方法打开处理文件帮我我们做了什么？--------------------------')
# f = open("","wd")
# try:
#     f.write("hello")
# except:
#     pass
# finally:
#     f.close()
print('''打开文件在进行读写的时候可能会出现一些异常状况
，如果按照常规的f.open
写法，我们需要try,except,finally，
做异常判断，并且文件最终不管遇到什么情况，
都要执行finally f.close()关闭文件，with方法帮我们实现了finally中f.close''')

print('10、-----------------列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]--------------------------')
print('map（）函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写，根据需求')
list_02 = [1,2,3,4,5]
def fn(x):
    return x**2
res = map(fn,list_02)
res = [i for i in res if i>10]
print(res)

print('11、-----------------python中生成随机整数、随机小数、0--1之间小数方法--------------------------')
print('''
1/随机整数：random.randint(a,b),生成区间内的整数
2/随机小数：习惯用numpy库，利用np.random.randn(5)生成5个随机小数
3/0-1随机小数：random.random(),括号中不传参
''')
import random
import numpy
result = random.randint(1,20)
print(result)

print('12、-----------------避免转义给字符串加哪个字母表示原始字符串？--------------------------')
print('r , 表示需要原始字符串，不转义特殊字符')
print('13、-----------------python中断言方法举例--------------------------')
print('assert（）方法，断言成功，则程序继续执行，断言失败，则程序报错')
# a = 3
# assert (a>3)
# print("断言成功，则程序继续执行")
# a = 4
# assert (a>5)
# print("断言失败，则程序报错")
print('14、-----------------数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句--------------------------')
# print("select distinctname  from  student")
print('15、-----------------10个Linux常用命令--------------------------')
print('ls  pwd  cd  touch  rm  mkdir  tree  cp  mv  cat  more  grep  ech')
print('16、-----------------列出python中可变数据类型和不可变数据类型，并简述原理--------------------------')

print('''
不可变数据类型：数值型、字符串型string和元组tuple
不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，
在内存中则只有一个对象（一个地址），如下图用id()方法可以打印对象的id
''')
print('''
不可变数据类型：可变数据类型：列表list和字典dict；

允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，
只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，
不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，
相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象。
''')
a = 3
b = 3
print(id(a))
print(id(b))
c =[1,2]
n =[1,2]
print(id(c))
print(id(n))
print('17、-----------------s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"--------------------------')
print('''
set去重，去重转成list,利用sort方法排序，reeverse=False是从小到大排
list是不 变数据类型，s.sort时候没有返回值，所以注释的代码写法不正确
''')
s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort(reverse = False)
# s = s.sort(reverse = False)    s.sort时候没有返回值，所以注释的代码写法不正确
res = "".join(s)
print(res)

print('18、-----------------用lambda函数实现两个数相乘--------------------------')
sum = lambda a,b:a*b  #(a,b)参数，(a*b)表达式
print(sum(4,5))

print('19、-----------------字典根据键从小到大排序--------------------------')
dic_02={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
list_03 = sorted(dic_02.items(),key=lambda i:i[0],reverse=False)
print(list_03)
print(dict(list_03))
print('20、-----------------利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"--------------------------')
from collections import Counter
a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(a)
print(res)

print('21、-----------------字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"--------------------------')
import re
a = "not 404 found 张三 99 深圳"
list = a.split(" ")
print(list)
res = re.findall('\d+\.?d*|[a-zA-Z]+',a)
for i in res:
    if i in list:
        list.remove(i)
new_str = " ".join(list)
print(res)
print(new_str)

print('22、-----------------filter方法求出列表所有奇数并构造新列表--------------------------')

print('''
filter() 函数用于过滤序列，过滤掉不符合条件的元素，
返回由符合条件元素组成的新列表。该接收两个参数，
第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
然后返回 True 或 False，最后将返回 True 的元素放到新列表
''')
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fun_01(a):
    return a%2==1
new_list =filter(fun_01,a)
new_list = [i for i in new_list]
print(new_list)

print('23、-----------------列表推导式求列表所有奇数并构造新列表--------------------------')
b =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i for i in b if i%2==1]
print(res)
print('24、-----------------正则re.complie作用--------------------------')
print('''re.compile是将正则表达式编译成一个对象，加快速度，并重复使用''')

print('25、-----------------a=（1，）b=(1)，c=("1") 分别是什么类型的数据？--------------------------')

print(type(1))
print(type((1,)))
print(type("1"))
print('26、-----------------两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]--------------------------')
print('''extend可以将另一个集合中的元素逐一添加到列表中，区别于append整体添加''')
a= [1,5,7,9]
b =[2,2,6,8]
a.extend(b)
print(a)
a.sort(reverse=False)
print(a)

print('27、-----------------用python删除文件和用linux命令删除文件方法--------------------------')
print('''python：os.remove(文件名)

linux:       rm  文件名''')
print('28、-----------------log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳--------------------------')
import datetime
a =str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"  星期："+str(datetime.datetime.now().isoweekday())
print(a)
print('29、-----------------数据库优化查询方法--------------------------')
print('''外键、索引、联合查询、选择特定字段等等''')

print('30、-----------------请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行--------------------------')
print('''pychart、matplotlib''')

print('31、-----------------写一段自定义异常代码--------------------------')
print('''自定义异常用raise抛出异常''')
def test_01():
    try:
        for i in range(5):
            if i >4:
                raise Exception("数字大于2")
    except Exception as ret:
        print(ret)
test_01()

print('31、-----------------正则表达式匹配中，（.*）和（.*?）匹配区别？--------------------------')
print('''（.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配

（.*?）是非贪婪匹配，会把满足正则的尽可能少匹配''')
s = "<a>哈哈</a><a>呵呵</a>"
res1 = re.findall("<a>(.*)</a>",s)
print(res1)
res2 = re.findall("<a>(.*?)</a>",s)
print(res2)
print('32、-----------------简述Django的orm--------------------------')
print(''''ORM，全拼Object-Relation Mapping，意为对象-关系映射
实现了数据模型与数据库的解耦，通过简单的配置就可以轻松更换数据库，
而不需要修改代码只需要面向对象编程,orm操作本质上会根据对接的数据库引擎，
翻译成对应的sql语句,所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，
如果数据库迁移，只需要更换Django的数据库引擎即可''')
print('33、-----------------[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]--------------------------')
a = [[1,2],[3,4],[5,6]]
x=[j for i in a for j in i]
print(x)
print('''还有更骚的方法，将列表转成numpy矩阵，通过numpy的flatten（）方法''')
import numpy as np
b = np.array(a).flatten().tolist()
print(b)
print('34、-----------------举例说明异常模块中try except else finally的相关意义--------------------------')
print('''try..except..else没有捕获到异常，执行else语句''')
try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误：%s'%errorMsg)
else:
    print('没有捕获异常，执行该语句')
print('''try..except..finally不管是否捕获到异常，都执行finally语句''')
try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误：%s'%errorMsg)
finally:
    print('不管是否捕获异常，执行该语句')
print('35、-----------------a="张明 98分"，用re.sub，将98替换为100--------------------------')
a="张明 98分"
ret = re.sub(r"\d+","100",a)
print(ret)

print('36、-----------------提高python运行效率的方法--------------------------')
print('''
1、使用生成器，因为可以节约大量内存
2、循环代码优化，避免过多重复代码的执行
3、核心模块用Cython  PyPy等，提高效率
4、多进程、多线程、协程
5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率''')

print('37、-----------------简述mysql和redis区别--------------------------')
print('''1、细节上的错误，通过print（）打印，能执行到print（）说明一般上面的代码没有问题，分段检测程序是否有问题，如果是js的话可以alert或console.log
2、如果涉及一些第三方框架，会去查官方文档或者一些技术博客。
3、对于bug的管理与归类总结，一般测试将测试出的bug用teambin等bug管理工具进行记录，然后我们会一条一条进行修改，修改的过程也是理解业务逻辑和提高自己编程逻辑缜密性的方法，我也都会收藏做一些笔记记录。
4、导包问题、城市定位多音字造成的显示错误问题''')
print('38、-----------------简述mysql和redis区别--------------------------')
print('''
redis： 内存型非关系数据库，数据保存在内存中，速度快
mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的Io操作，访问速度相对慢''')
print('39、-----------------list=[2,3,5,4,9,6]，从小到大排序，不许用sort--------------------------')
list = [2,3,4,5,8,9,2,3]
new_list =[]
def get_min(list):
    a =min(list)
    list.remove(a)
    new_list.append(a)
    if len(list)>0:
        get_min(list)
        return new_list
new_list = get_min(list)
print(new_list)

print('40、-----------------保留两位小数--------------------------')
a="%.03f"%1.3335
print(a,type(a))
res = round(float(a),2)
print(res)
print('41、-----------------列出常见的状态码和意义--------------------------')
print(
    '''
200 OK      请求正常处理完毕
204 No Content      请求成功处理，没有实体的主体返回
206 Partial Content           GET范围请求已成功处理
301 Moved Permanently           永久重定向，资源已永久分配新URI
302 Found            临时重定向，资源已临时分配新URI
303 See Other          临时重定向，期望使用GET定向获取
304 Not Modified           发送的附带条件请求未满足
307 Temporary Redirect          临时重定向，POST不会变成GET
400 Bad Request           请求报文语法错误或参数错误
401 Unauthorized           需要通过HTTP认证，或认证失败
403 Forbidden              请求资源被拒绝
404 Not Found           无法找到请求资源（服务器无理由拒绝）
500 Internal Server Error        服务器故障或Web应用故障
503 Service Unavailable        服务器超负载或停机维护'''
)
print('42、-----------------使用pop和del删除字典中的"name"字段--------------------------')
dic={"name":"zs","age":18}
dic.pop("name")
print(dic)
dic={"name":"zs","age":18}
del dic["name"]
print(dic)
print('43、-----------------简述cookie和session的区别--------------------------')
print('''
1，session 在服务器端，cookie 在客户端（浏览器）
2、session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，如果浏览器禁用了 cookie ，
同时 session 也会失效，存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置
3、cookie安全性比session差''')

print('44、-----------------简述多线程、多进程--------------------------')
print('''进程：
1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制''')
print('''
线程：
1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，一个进程下的多个线程可以共享该进程的所有资源
2、如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃''')
print('45、-----------------IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常--------------------------')
print('''
IOError：输入输出异常
AttributeError：试图访问一个对象没有的属性
ImportError：无法引入模块或包，基本是路径问题
IndentationError：语法错误，代码没有正确的对齐
IndexError：下标索引超出序列边界
KeyError:试图访问你字典里不存在的键
SyntaxError:Python代码逻辑语法出错，不能执行
NameError:使用一个还未赋予对象的变量
''')
print('46、-----------------python中copy和deepcopy区别--------------------------')
print('''''')
print('47、-----------------a = "  hehheh  ",去除收尾空格--------------------------')
a = "  hehheh  "
a.strip()
print(a)
print('48、-----------------举例sort和sorted对列表排序--------------------------')
print('''sort在列表基础上修改，没有返回值
sorted有返回值是最新的list
''')
print('49、-----------------HTTP请求中get和post区别--------------------------')
print('''1、GET请求是通过URL直接请求数据，数据信息可以在URL中直接看到，比如浏览器访问；而POST请求是放在请求头中的，我们是无法直接看到的；
2、GET提交有数据大小的限制，一般是不超过1024个字节，而这种说法也不完全准确，HTTP协议并没有设定URL字节长度的上限，而是浏览器做了些处理，
所以长度依据浏览器的不同有所不同；POST请求在HTTP协议中也没有做说明，一般来说是没有设置限制的，但是实际上浏览器也有默认值。总体来说，少量的数据使用GET，大量的数据使用POST。
3、GET请求因为数据参数是暴露在URL中的，所以安全性比较低，比如密码是不能暴露的，就不能使用GET请求；POST请求中，
请求参数信息是放在请求头的，所以安全性较高，可以使用。在实际中，涉及到登录操作的时候，尽量使用HTTPS请求，安全性更好。''')

print('27、-----------------python中读取Excel文件的方法--------------------------')
123
import pandas
print(c)
print('27、-----------------用python删除文件和用linux命令删除文件方法--------------------------')
print('27、-----------------用python删除文件和用linux命令删除文件方法--------------------------')
print('27、-----------------用python删除文件和用linux命令删除文件方法--------------------------')
print('27、-----------------用python删除文件和用linux命令删除文件方法--------------------------')

