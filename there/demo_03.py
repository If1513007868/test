from urllib.parse import urlparse,quote

print(quote('中国'))
#解析URL
obj = urlparse('https://baike.baidu.com/item/统一资源定位系统/5937042?fromtitle=url&fromid=110640')
print(obj)
print(obj.path)
print(obj.scheme)
print(obj.netloc)


