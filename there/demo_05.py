import requests
from bs4 import BeautifulSoup
import queue

start_page = "http://www.163.com"  #起始页
domain = "163.com"
url_queue = queue.Queue()  #队列
seen = set()  #集合用来去重

seen.add(start_page)
url_queue.put(start_page)  #页面放到队列


def sotre(url):
    pass

def extract_urls(url):  #解析页面
    urls = []
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    for e in soup.findAll('a'):  #a标签
        url = e.attrs.get('href', '#')
        urls.append(url)   #放到列表
    return urls



while True:

    if not url_queue.empty():

        current_url = url_queue.get()
        print(current_url)
        sotre(current_url)
        for next_url in extract_urls(current_url):
            if next_url not in seen and domain in next_url:
                seen.add(next_url)
                url_queue.put(next_url)
    else:
        break