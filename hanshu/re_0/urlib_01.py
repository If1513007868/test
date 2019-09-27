import requests
from urllib import request,parse,error
import json
from urllib.parse import urlparse,urlunparse,urljoin,urlencode

#-----------------------爬虫基础模块--------------------------
# ==================一、urllib 文档
# 1.request： 他是最基本的http请求模块，可以用来发送请求，取得相应结果
# 2.error： 异常处理模块，如果请求出错我们可以捕获异常，进行处理
# 3.parse： 对url进行处理
#      urlopen()

r = request.urlopen("https://www.163.com")
#r 是个HTTPResponse类的对象，主要包含read()、getheader(name)、getheaders()、info()、等方法，
# 以及msg、version、status、reason

#print(r.read().decode('gbk'))
print(r.status)
print(r.getheaders())
print(r.getheader('Server'))

print('--------------data----------------')

# --------data参数
# 发送一个表单请求 application/x-www-form-urlencoded
# data = bytes(parse.urlencode({'name': 'test','password':'123456'}), encoding='utf-8')
# r = request.urlopen('http://httpbin.org/post', data=data)
# print(r.read().decode())

print('--------------timeout----------------')
#------timeout参数指定超时时间，单位是秒，如果超过了这个时间还没有得到响应就抛出异常
# try:
#     r = request.urlopen('http://httpbin.org/get',timeout=(0.1))
#     print(r.read().decode())
# except error.URLError as e:
#     print(e.reason)
print('-------------自定义header,发送json-----------------')
# url = 'http://httpbin.org/post'
# headers = {
# 'User-Agent': 'Mozilla/4.0',
# 'Content-Type': 'application/json'
# }
# d = {'name': 'test'}
# data = bytes(parse.urlencode(d), encoding='utf-8')
# req = request.Request(url,data,headers,method='POST')
# r = request.urlopen(req)
# print(r.read().decode())

# print('-------------发送json-----------------')
# from urllib import request
# import json
#
# headers = {
#         'Content-Type': 'application/json',
# }
# data = json.dumps({'name': 'test'})
# rt = request.Request('http://httpbin.org/post', headers=headers, data=bytes(data, encoding='utf-8'))
# r = request.urlopen(rt)


print('-------------解析链接urlparse-----------------')
result = urlparse('http://www.baidu.com/inex.html;user?id=5#comment')
print(result)
print('-------------解析链接unurlparse-----------------')
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
print('-------------解析链接urljoin-----------------')
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print('-------------解析链接urlencode-----------------')
d = {'name': 'test'}
print(urlencode(d))
print(bytes(urlencode(d),encoding='utf-8'))






