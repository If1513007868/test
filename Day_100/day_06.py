#文件和异常

# /Users/mac/Desktop/ce_data/123.txt

# def main():
#     f= None
#     try:
#         f = open('/Users/mac/Desktop/ce_data/123.txt', 'r',encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件!')
#     except LookupError:
#         print('指定了未知的编码!')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误!')
#     finally:
#         if f:
#             f.close()

# 在Python中，我们可以将那些在运行时可能会出现状况的代码放在try代码块中，
# 在try代码块的后面可以跟上一个或多个except来捕获可能出现的异常状况。例如
# 在上面读取文件的过程中，文件找不到会引发FileNotFoundError，
# 指定了未知的编码会引发LookupError，而如果读取文件时无法按指定方式解码会引发UnicodeDecodeError，
# 我们在try后面跟上了三个except分别处理这三种不同的异常状况。最后我们使用finally代码块来关闭打开的文件，
# 释放掉程序中获取的外部资源，由于finally块的代码不论程序正常还是异常都会执行到（甚至是调用了sys模块的exit函数退出Python环境，
# finally块都会被执行，因为exit函数实质上是引发了SystemExit异常），因此我们通常把finally块称为“总是执行代码块”，
# 它最适合用来做释放外部资源的操作。如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，
# 通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源，代码如下所示。
#
# main()
def main():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')
#
# import requests
# def mai():
#     resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
#     data_model = json.loads(resp.text)
#     for news in data_model['newslist']:
#         print(news['title'])



if __name__ == '__main__':
    main()

