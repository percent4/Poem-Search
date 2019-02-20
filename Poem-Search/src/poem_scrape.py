# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 爬取的诗歌网址
urls = ['https://www.gushiwen.org/gushi/tangshi.aspx',
        'https://www.gushiwen.org/gushi/sanbai.aspx',
        'https://www.gushiwen.org/gushi/songsan.aspx',
        'https://www.gushiwen.org/gushi/songci.aspx'
        ]

poem_links = []
# 诗歌的网址
for url in urls:
    # 请求头部
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.text, "lxml")
    content = soup.find_all('div', class_="sons")[0]
    links = content.find_all('a')

    for link in links:
        poem_links.append(link['href'])

# print(poem_links)
# print(len(poem_links))

content_list = []
title_list = []
dynasty_list = []
poet_list = []

# 爬取诗歌页面
def get_poem(url):
    #url = 'https://so.gushiwen.org/shiwenv_45c396367f59.aspx'
    # 请求头部
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")

    # 诗歌内容
    poem = soup.find('div', class_='contson').text.strip()
    poem = poem.replace(' ', '')
    poem = re.sub(re.compile(r"\([\s\S]*?\)"), '', poem)
    poem = re.sub(re.compile(r"（[\s\S]*?）"), '', poem)
    poem = re.sub(re.compile(r"。\([\s\S]*?）"), '', poem)
    poem = poem.replace('!', '！').replace('?', '？').replace('\n', '')
    content = poem

    if content:
        content_list.append(content)
    else:
        content_list.append('')

    # 诗歌朝代，诗人
    dynasty_poet = soup.find('p', class_='source').text
    if '：' in dynasty_poet:
        dynasty, poet = dynasty_poet.split('：')
    else:
        dynasty, poet = '', ''

    dynasty_list.append(dynasty)
    poet_list.append(poet)

    # 诗歌标题
    title = soup.find('h1').text
    if title:
        title_list.append(title)
    else:
        title_list.append('')

# 爬取诗歌
for url in poem_links:
    get_poem(url)

# 写入至csv文件
df = pd.DataFrame({'title': title_list,
                   'dynasty': dynasty_list,
                   'poet': poet_list,
                   'content': content_list
                   })
print(df.head())

df.to_csv('./poem.csv', index=False)
