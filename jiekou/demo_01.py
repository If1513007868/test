import requests
import json
# par = {"Keywords":"yoyoketang"}
# r = requests.get("https://www.cnblogs.com/yoyoketang/",params=par)
# print(r.status_code)
# print(r.text)

r = requests.get("https://www.baidu.com",)
print(r.status_code)
print(r.url)
print(r.encoding)  #编码
print(r.content)  #获取返回内容（自动解码gzip）
print("头信息                ",r.headers)    #以字典存储的信息头，不存在返回None
print("cookie               ",r.cookies)
#print(r.json())    #内置的json解码器
print(r.raw)      #返回原始响应体
print(r.raise_for_status())    #失败请求非200抛出异常