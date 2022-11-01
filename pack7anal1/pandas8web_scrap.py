# 웹문서 읽기

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

print('벅스 차트 출력하기 ----') 

url = urlopen("https://music.bugs.co.kr/chart")
soup = BeautifulSoup(url.read(), 'html.parser')
# print(soup)
musics = soup.find_all('td', class_='check')
# print(musics)
for i, music in enumerate(musics):
    print("{}위:{}".format(i+1, music.input['title']))
    
    

print()
# 웹문서 읽기 2
import urllib.request as req
url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
wiki = req.urlopen(url)
print(wiki)
soup2 = BeautifulSoup(wiki, 'html.parser')
#print(soup2)
print(soup2.select("div.mw-parser-output > p > b"))
result = soup2.select("div.mw-parser-output > p > b")
for a in result:
    print(a.string)

print('--------------')
# 웹문서 읽기 3 - 다음 뉴스 읽어오기
url="https://news.daum.net/society#1"
daum = req.urlopen(url)
soup3= BeautifulSoup(daum, 'lxml')
print(soup3.select_one("div > strong > a"))
data = soup3.select_one("div > strong > a")
for i in data:
    print(i)

print()
datas = soup3.select("div > strong > a")
for i in datas[:5]:
    print(i)

print()
datas2 = soup3.findAll("a")
for i in datas2[:5]:
    #print(i)
    h = i.attrs['href']
    t = i.string
    print('href:%s, text:%s'%(h,t))











