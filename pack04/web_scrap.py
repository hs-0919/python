# 멀티 프로세싱으로 웹 스크래핑
# https://beomi.github.io/beomi.github.io_old/        # 연습용 사이트

import requests # - 웹에 접근할때
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool


def get_links():    # a tag의 주소를 읽기
    data=requests.get('https://beomi.github.io/beomi.github.io_old/').text
    soup=bs(data,'html.parser')
    # print(soup)
    my_titles = soup.select(
        'h3> a'
        )
    # 파일을 읽을때 h3형식..?
    data =[]
    
    for title in my_titles:
        data.append(title.get('href'))
    return data
    
    
def get_content(link):  # a tag에 의한 해당 사이트 문서 내용 중 일부 문자값 읽기
    abs_link = 'https://beomi.github.io' + link
    # print(abs_link)
    req = requests.get(abs_link)
    html = req.text
    soup = bs(html, 'html.parser')
    #가져온 자료로 뭔가를 할 수 있음~
    print(soup.select('h1')[0].text)
    
    
if __name__=='__main__':
    start_time=time.time()
    #print(get_links())
    #print(len(get_links()))
    
    
    ''' 직렬 처리 " 0.9초
    for link in get_links():
        get_content(link)
    '''    
    
    pool = Pool(processes=4)  #병렬 처리 - 0.59초
    pool.map(get_content, get_links())
    
    
    
    print('처리 시간: {}'.format(time.time() - start_time))