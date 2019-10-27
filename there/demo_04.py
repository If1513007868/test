from bs4 import BeautifulSoup
import requests


url = "https://movie.douban.com/"

r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')

element = soup.select('#billboard > div.billboard-bd > table')[0]  #查看源代码找元素
for item in element.find_all('a'):
    print(item.text)

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title)
print(soup.p)
print(soup.p['class'])
print(soup.find_all('a'))