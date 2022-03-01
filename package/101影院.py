# coding:utf-8
import random

import requests
from bs4 import BeautifulSoup

# 81影院

page = 1
maxPage = 507
file_handle = open('../dev/101影院.txt', mode='w')
while page <= maxPage:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
    # 添加随机用户请求信息，防止大量‍同一用户请求被拒
    headers['User-Agent'] = random.choice(user_agent_list)
    url = 'https://www.101yingyuan.net/vod/list21-' + str(page) + '.html'
    fileUrl = 'https://www.101yingyuan.net'
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    content = r.text
    soup = BeautifulSoup(content, "html.parser")
    for tag in (soup.find('div', class_='vodlist_l box').find_all('ul')):
        title = tag.find('h2').find('a').string.encode('UTF-8')
        img = tag.find('img').get('data-original').encode('UTF-8')
        url = fileUrl + tag.find('a').get('href').encode('UTF-8')
        file_handle.write(str(title) + "   " + img + "  " + url + "  \n")
        print (str(page) + "  " + str(title) + "   " + img + "  " + url + "  ")
    page += 1
