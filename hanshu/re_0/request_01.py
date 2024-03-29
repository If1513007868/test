import requests
from lxml import etree
from bs4 import BeautifulSoup

#
# print(htmlEmt.xpath("//li"))
# print(htmlEmt.xpath("//li/a"))
# 通过属性定位
# print(htmlEmt.xpath('//li[@class="item-0"]'))
# 获取属性值
# print(htmlEmt.xpath('//li/@class'))
# 获取文本
# print(htmlEmt.xpath('//li/a[@href="link1.html"]//text()'))

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title)
print(soup.p)
print(soup.p['class'])
print(soup.find_all('a'))
