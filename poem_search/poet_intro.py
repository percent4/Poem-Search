# -*- coding: utf-8 -*-

import re
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import requests

class PoetSearch(object):

    def __init__(self, person):
        self.person = person

    def search(self):
        if self.person:
            try:
                # print(self.person)
                url = 'http://baike.baidu.com/item/' + urllib.parse.quote(self.person)
                # 请求头部
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, \
                            like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
                req = requests.get(url, headers=headers)

                # print(req.status_code)
                if str(req.status_code) == '200':
                    soup = BeautifulSoup(req.text.encode('ISO-8859-1'), "lxml")
                    text = list(soup.find('div', class_="lemma-summary").children)
                    content = ''
                    for para in text:
                        x = str(para).replace('\n', '')
                        word = re.sub(re.compile(r"<(.+?)>"), '', x)
                        words = re.sub(re.compile(r"\[(.+?)\]"), '', word)
                        if words:
                            content += words+'*'
                    return content
                else:
                    return 'HTTP请求失败，错误状态码为：%s' % str(req.status_code)
            except AttributeError:
                return "搜索有误，请换个名词重新尝试~"
            except Exception as err:
                print("ERROR: %s" % err)
                return "搜索有误~"
        else:

            return ""

    def search_image(self):
        if self.person:
            try:
                # print(self.person)
                url = 'http://baike.baidu.com/item/' + urllib.parse.quote(self.person)
                # 请求头部
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, \
                            like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
                req = requests.get(url, headers=headers)

                # print(req.status_code)
                if str(req.status_code) == '200':
                    soup = BeautifulSoup(req.text.encode('ISO-8859-1'), "lxml")
                    pic_url = soup.find('div', class_="summary-pic")('img')[0]['src']
                    return pic_url
                else:
                    return ""
            except AttributeError:
                return ""
            except Exception as err:
                print("ERROR: %s" % err)
                return ""
        else:

            return ""


# a = PoetSearch('杜甫').search()
# print(a)
PoetSearch('杜甫').search_image()