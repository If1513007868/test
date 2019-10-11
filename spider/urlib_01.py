# request： 他是最基本的http请求模块，可以用来发送请求，取得相应结果
# error： 异常处理模块，如果请求出错我们可以捕获异常，进行处理
# parse： 对url进行处理

# r 是个HTTPResponse类的对象，
# 主要包含read()、getheader(name)、getheaders()、info()、等方法，以及msg、version、status、reason等属性

from urllib import request,parse,error
import json
try:
    r = request.urlopen("https://www.163.com",timeout=0.5)
except error.URLError as e:
    print(e.reason)

#print(r.read().decode('gbk'))
print(r.status)
#print(r.getheaders())
print(r.getheader('Server'))
print(r.info())  #打印的是header信息
print(r.version)

# print(r.reason)
# print(r.msg)
print('--------------------------data----------------------------------')

# data参数是可选的，设置了该参数请求方法就不再是get而是post
# 发送一个表单请求 application/x-www-form-urlencoded
data = bytes(parse.urlencode({'name': 'test'}), encoding='utf-8')
r = request.urlopen('http://httpbin.org/post', data=data,timeout=2)
print(r.read().decode())
print('--------------------------异常处理----------------------------------')
try:
    r = request.urlopen('http://httpbin.org/get', timeout=0.1)
    print(r.read().decode())
except error.URLError as e:
    print(e.reason)
print('--------------------------Request类来构造一个请求----------------------------------')
#Request 上面的方法可以完成一些简单的请求如何get和post表单，不能设置header，
#不支持其它请求方法 如果需要自定义header或put、delete等方法就需要使用Request类来构造一个请求
rt = request.Request('https://python.org')
re = request.urlopen(rt)
#print(re.read().decode())

print('--------------------------自定义header----------------------------------')


url = 'http://httpbin.org/post'
headers = {
        'User-Agent': 'Mozilla/4.0',
}
d = {'name': 'test'}
data = bytes(parse.urlencode(d), encoding='utf-8')

req = request.Request(url,data,headers,method='POST')
r = request.urlopen(req)

print(r.read().decode())
print('--------------------------发送json---------------------------------')
headers = {
    'Content-Type': 'application/json',
}
data = json.dumps({'name': 'test'})
rt = request.Request('http://httpbin.org/post',headers=headers,data = bytes(data,encoding='utf-8'))
r = request.urlopen(rt)
print(r.read().decode())

