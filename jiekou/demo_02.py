import requests
import json
url = 'http://172.16.20.152:7040/api/ec/login'
hearders ={
        "Content-Type":"application/json",
        "User-Agent":"PostmanRuntime/7.17.1",
        "Accept":"*/*",
        "Cache-Control":"no-cache",
        "Postman-Token":"23356de5-b5d9-4ee1-8554-c792b90bcbb8",
        "Host":"172.16.20.152:7040",
        "Accept-Encoding":"gzip, deflate",
        "Content-Length":"72",
        "Connection":"keep-alive"
}
payload = {
    "credential": 123456,
    "phone": 15130078689,
    "type": "PASSWARD"
}
data_json = json.dumps(payload)
r = requests.post(url,hearders=hearders,json=data_json,verify=False)
result = r.content
print(result)




