# 네이버 제공 코스피 정보를 읽어 csv 파일로 저장

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
fname = "네이버_코스피.csv"
# fObj = open(fname, mode='w', encoding='UTF-8', newline='') # 공백행 제외
fObj = open(fname, mode='w', encoding='UTF-8-sig', newline='') # 엑셀에서 한글깨짐 방지
writer = csv.writer(fObj)
title="N    종목명    현재가    전일비    등락률    액면가    시가총액    상장주식수    외국인비율    거래량    PER    ROE    토론실".split()
print(title)
writer.writerow(title)

for page in range(1, 3):
    res = requests.get(url.format(str(page)))
    res.raise_for_status() # 읽기 실패하면 작업 중지 
    soup = BeautifulSoup(res.text, 'html.parser')
    datas = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    
    for row in datas:
        cols = row.findAll("td")
        if len(cols) <= 1:continue  # [''] 해결
        data = [col.get_text().strip() for col in cols] # strip() : '\n\n\n\n\n\n ... ' 제거
        print(data)
        writer.writerow(data)
fObj.close()

# csv 읽기
import pandas as pd
from urllib.request import urlopen
df = pd.read_csv(fname)
print(df.head(5))

# 웹툰

url = "https://comic.naver.com/webtoon?tab=tue"
fname = '네이버_인기웹툰순위.csv'
#fObj = open(fname, mode='w', encoding='utf-8', newline='') # 공백행 제외
fObj = open(fname, mode='w', encoding='utf-8-sig', newline='') # 엑셀에서 읽을 때 한글 깨짐
writer = csv.writer(fObj)
title = '인기순'.split()
print(title)
writer.writerow(title)

res = requests.get(url)
print(res)

res.raise_for_status() # 읽기 실패하면 작업 중지

soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
datas = soup.find('ul',attrs={'class':'AsideList__content_list--FXDvm'}).findAll('li')
print(datas)

for row in datas:
    cols = row.findAll('a')
    print(cols)
    # if len(cols) <= 1:continue  # [''] 해결
    data = [col.get_text().strip() for col in cols] # .strip() 공백 제거를 해야함
    print(data)
    writer.writerow(data) # 데이터를 파일로 저장

fObj.close()


    
    
    