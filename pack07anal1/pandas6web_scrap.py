# 웹 문서 읽기 - scraping
# crawling : scrap, selenium,...
# Beautifulsoup을 이용하기: XML, HTML 문서 처리

# 
import requests
from bs4 import BeautifulSoup

def spider():
    baseUrl ="https://www.naver.com/index.html"
    sourceData = requests.get(baseUrl)
    print(sourceData)
    
    plainText = sourceData.text
    # print(plainText)
    print(type(plainText))  # <class 'str'>
    
    # 객체로 만들기
    convertData=BeautifulSoup(plainText, 'lxml') # BeautifulSoup(  , [html.parser,lxml,xml] 셋중 하나사용)
    # print(convertData)
    print(type(convertData))  # <class 'bs4.BeautifulSoup'>
    
    for atag in convertData.find_all('a'):
        href =atag.get('href')
        title = atag.string
        print(href, ' ', title)
    
    
    
    


if __name__ == '__main__':
    spider()









