# import pandas as pd
# from pandas import Series, DataFrame
# import numpy as np
#
# obj= np.random.randn(9, 4)
# print(obj)
# print(DataFrame(obj, columns=['No1', 'No2', 'No3', 'No4']))
# print(obj.mean(axis=0))
# print()
#
#
# obj1=pd.DataFrame([[i] for i in range(10, 41, 10)], columns=['numbers'], index=['a','b','c','d'])
# print(obj1)
# print()
# print(obj1.iloc[2])
'''
import csv
import requests
from bs4 import BeautifulSoup

url2="https://comic.naver.com/index"
webtoon = requests.get(url2).text
soup4 = BeautifulSoup(webtoon, 'html.parser')
#realTimeRankFavorite > li.rank01
datas2 = soup4.find("ol", attrs={"id":"realTimeRankFavorite"}).find_all("li")
    
for i, data in enumerate(datas2):
    d=data.find("a").get_text()
    print("{}위 : {}".format(i+1, d))
'''

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
url = "http://www.kyochon.com/menu/chicken.asp"
chicken = urllib.request.urlopen(url).read()
soup = BeautifulSoup(chicken, 'html.parser')
# print(soup)
data = soup.find('ul',attrs={'class':'menuProduct'}).findAll('li')
# print(data)
df = pd.DataFrame(data)
for a in data:
    name=a.find('dt').text
    price=a.find('strong').text
    print('치킨 명 :', name)
    print('가격 : ', price)
#tabCont01 > ul > li:nth-child(1) > a > p.money > strong

