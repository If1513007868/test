
# 爬虫前奏（原生爬虫）
# #1.明确抓取的目的
# 2.找到数据对应的网页
# 3分析网页结构，找到数据所在的标签位置
#
# 模拟http请求，向服务器发送个请求，获取服务器返回给我们的html
# 用正则表达式提取我们的数据（名字，人气）
from urllib import request
#断点调试

class spider():
    url = "https://www.baidu.com"
    def __fetch_content(self): #私有函数
        r = request.urlopen(spider.url)   #读取类变量的方法spider.url
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        a = 1
    def __analysis(self,htmls):
        pass
    def go(self):
        htmls = self.__fetch_content()

spider = spider() #实例化
spider.go()