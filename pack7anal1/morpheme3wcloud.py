# 웹문서에서 검색된 자료 스크래핑 후 형태소 분석하고 난 다음 워드클라우드 작성
# donga.com에서 검색

# pip install pygame
# pip install simplejson
# pip install pytagcloud

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
from konlpy.tag import Okt
from collections import Counter  # 카운팅 지원 모듈
import pytagcloud
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scrapy import item

# keyword = input('검색어 : ')
keyword = '낙옆' # 보수 좌파
targetUrl = "https://www.donga.com/news/search?query=" + quote(keyword)
print(targetUrl)  # https://www.donga.com/news/search?query=%EB%B6%81%ED%95%9C%EB%82%99%EC%98%86

source = urllib.request.urlopen(targetUrl)
soup = BeautifulSoup(source, 'lxml', from_encoding='utf-8')
# print(soup)

msg = ""

for title in soup.find_all('p', 'tit'):
    title_link = title.select('a')
    # print(title_link)
    articleUrl = title_link[0]['href']
    # print(articleUrl)
    try:
        source_article = urllib.request.urlopen(articleUrl)
        soup = BeautifulSoup(source_article, 'lxml', from_encoding='utf-8')
        contents = soup.select('div.article_txt')
        # print(contents)
        for imsi in contents:
            item = str(imsi.find_all(text=True))
            # print(item)
            msg = msg + item
            
    except Exception as e:
        pass

print(msg)






