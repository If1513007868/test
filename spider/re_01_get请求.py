import requests
data = {'name': 'test', 'age': 18}  #带参数的get请求
#r = requests.post("http://httpbin.org/post", data=data)   post请求

r = requests.get("https://www.baidu.com")
print(r.text)
print(r.status_code)
print(r.cookies)