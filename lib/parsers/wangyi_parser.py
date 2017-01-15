from bs4 import BeautifulSoup
from lib.parsers.parser import Parser
from lib import spider
import re

class WangyiParser(Parser):
    __domain = 'https://manhua.163.com/'
    __re_imgurl = re.compile(r'\{[\w:",\.\(\)\s]+url:[\w\.\s]+\?\s*"https://[\w\./=%&\?]+"\s*:\s*"(https://[\w\./=%&\?]+)"[\w:",\.\(\)\s]+\}')

    def fetch(self, id):
        html = spider.get(self.__domain + 'source/' + id)
        soup = BeautifulSoup(html, 'html.parser')

        result = {}
        r = soup.select('.source-head > h1')
        if len(r) > 0:
            result['title'] = r[0].string

        r = spider.getJson(self.__domain + 'book/catalog/' + id + '.json')
        list = []
        if r:
            for item in r['catalog']['sections'][0]['sections']:
                sec = {
                    'name': item['title'],
                    'pages': self.__fetchImg(self.__domain + 'reader/' + id + '/' + item['sectionId'])
                }

                list.append(sec)

        result['list'] = list

        return result
    
    def __fetchImg(self, href):
        r = spider.get(href)
        list = []
        i = 1
        for m in self.__re_imgurl.finditer(r):
            list.append({
                'index': i,
                'href': m.group(1)
            })
            i += 1
        return list
