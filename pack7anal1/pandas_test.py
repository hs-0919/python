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
