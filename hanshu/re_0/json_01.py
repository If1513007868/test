import json

# JSON 数据解析
# # 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集
# # 它包含了两个函数  json.dumps(): 对数据进行编码/json.loads(): 对数据进行解码



# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)   #json.dumps(): 对数据进行编码
print("Python 原始数据：",repr(data))    #repr()输出原始数据
print("JSON 对象：",json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)   #json.loads(): 对数据进行解码
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])



# # 写入 JSON 数据
# with open('data.json', 'w') as f:
#     json.dump(data, f)
#
# # 读取数据
# with open('data.json', 'r') as f:
#     data = json.load(f)