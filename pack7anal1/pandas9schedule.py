# 일정 시간 마다 웹 문서 읽기

#import schedule # pip install schedule 스케줄러 모듈 지원
import time # 
import datetime
import urllib.request as req
from bs4 import BeautifulSoup
import requests

def work():
    url = "https://finance.naver.com/marketindex/"
    # data = req.urlopen(url)      # 방법 1 데이터를 보낼 때 인코딩하여 바이너리 형태로 보낸다 
    data = requests.get(url).text  # 방법 2 데이터를 보낼 때 딕셔너리 형태로 보낸다
    
    soup = BeautifulSoup(data, 'html.parser')
    # print(soup)
    price = soup.select_one("div.head_info > span.value").string
    print('미국USD : ', price)
    
    t = datetime.datetime.now()
    # print(t)
    fname = "./USD/" + t.strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
    # print(fname) ./USD/2022-11-01-12-57-55.txt
    
    with open(fname, 'w') as f:
        f.write(price)
while True:
    work()
    time.sleep(5)
    



