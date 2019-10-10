from urllib import request
r = request.urlopen("https://www.163.com")
print(r.read().decode('gbk'))
