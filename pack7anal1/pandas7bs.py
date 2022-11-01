# BeautifulSoup 클래스가 제공하는 searching 관련 method

from bs4 import BeautifulSoup


html_page = """
<html><body>
<h1>제목 태그</h1>
<p>웹문서 스크래핑</p>
<p>특정 페이지문서 읽기</p>
</body></html>
"""
print(type(html_page))

soup = BeautifulSoup(html_page, 'html.parser')
print(type(soup))
print(soup)

print()
h1 =soup.html.body.h1
print('h1:', h1)
print('h1:', h1.string)
print('h1:', h1.text)

print()
p1 = soup.html.body.p
print('p1:', p1.string)

p2 = p1.next_sibling.next_sibling
print('p2:', p2.string)

print('\n검색용 메소드 : find()')

html_page2 = """
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹문서 스크래핑</p>
<p id="my" class="our">특정 페이지문서 읽기</p>
</body></html>
"""

soup2 = BeautifulSoup(html_page2, 'html.parser')
print(soup2.p, ' ', soup2.p.string)
print(soup2.find('p').string)
print(soup2.find(['p', 'h1']).string)
print(soup2.find(id='title').string)
print(soup2.find(id='my').string)
print(soup2.find(class_='our').string)
print(soup2.find(attrs={'class':'our'}).string)
print(soup2.find(attrs={'id':'my'}).string)


print('\n검색용 메소드 : findAll(), find_all()')

html_page3 = """
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹문서 스크래핑</p>
<p id="my" class="our">특정 페이지문서 읽기</p>
<div>
    <a href="https://www.naver.com">naver</a><br/>
    <a href="https://www.daum.net">daum</a>
</div>
</body></html>
"""
soup3 = BeautifulSoup(html_page3, 'html.parser')
print(soup3.find_all('p'))
print(soup3.find_all('a'))
print(soup3.find_all(['a','p']))
print(soup3.find_all(class_='aa'))
print(soup3.findAll('p'))

print()
links=soup3.find_all('a')
for i in links:
    print(i.attrs['href'], ' - ', i.string)

print('정규 표현식')
import re
links2 = soup3.find_all(href=re.compile(r'^https'))

for i in links2:
    print(i.attrs['href'], ' - ', i.string)

print('\n CSS selector 사용 ')
html_page4 = """
<html><body>
<div id="hello">
    <a href="https://www.naver.com">naver</a><br/>
    <span>
        <a href="https://www.daum.net">daum</a>
    </span>
    <ul class="world">
        <li>안녕</li>
        <li>클레오파트라</li>
    </ul>
</div>
<div id="hi" class="good">
</body></html>
"""
soup4 = BeautifulSoup(html_page4, 'html.parser')
print(soup4.select_one("div")) # 단순 반환
print(soup4.select_one("div#hi"))
print(soup4.select_one("div.good"))
print()
print(soup4.select_one("div#hello > a")) # 복수 반환
print(soup4.select_one("div#hello a"))
print(soup4.select_one("div#hello > span >a"))

lis = soup4.select("div#hello ul.world> li")

print(lis)
msg = list()  # []
for i in lis:
    msg.append(i.string)
    
import pandas as pd
df = pd.DataFrame(msg, columns = ["자료"])
print(df)


