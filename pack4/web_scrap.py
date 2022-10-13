# 멀티 프로세싱으로 웹 스크래핑
# https://beomi.github.io/beomi.github.io_old/        # 연습용 사이트

import requests # - 웹에 접근할때
from bs4 import BeautifulSoup as bs
import time

def get_links():    # a tag의 주소를 읽기
    data=requests.get('https://beomi.github.io/beomi.github.io_old/').text
    soup=bs(data,'html.parser')
    # print(soup)
    # print(soup)
    my_titles = soup.select(
        'h3> a'
        )
    data =[]
    for title in my_titles:
        data.append(title.get('href'))
    return data
    
    
def get_content(link):  # a tag에 의한 해당 사이트 문서 내용 중 일부 문자값 읽기
    pass

if __name__=='__main__':
    start_time=time.time()
    print(get_links())
    print(len(get_links()))
    
    print('처리 시간: {}'.format(time.time() - start_time))