# 웹문서를 읽어서 형태소 분석(konlpy) 후 단어 빈도수 등을 출력

import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse # 한글 인코딩
okt = Okt()

# searchPara = input('검색단어 : ')
searchPara = "이순신"
searchPara = parse.quote(searchPara)
print(searchPara)


url = "https://ko.wikipedia.org/wiki/" + searchPara
page = urllib.request.urlopen(url).read().decode() # decode() , 인코딩, 시리얼라이징? 알아두기
# print(page)

soup = BeautifulSoup(page, 'lxml')
# print(soup)
wordlist = []  # 명사만 추출해서 기억
#mw-content-text > div.mw-parser-output > p:nth-child(6)
for item in soup.select("#mw-content-text > div.mw-parser-output > p"):
    # print(item.string)
    if item.string != None:
        wordlist += okt.nouns(item.string)
print('wordlist : ', wordlist, '단어 수 : ', len(wordlist))

# {'당시': 5, ... }
word_dict = {}  # 단어의 발생 횟수를 dict로 저장

for i in wordlist:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

print('발생 단어 수  : \n', word_dict)
print('발견된 단어 수(중복을 제거) : ' + str(len(set(wordlist))))

print('결과를 Series로 출력')
import pandas as pd

woList = pd.Series(wordlist)
print(woList[:3])
print(woList.value_counts()[:5])

print()
print('결과를 DataFrame으로 출력')
df1 = pd.DataFrame(wordlist, columns=['단어'])
print(df1.head(5))

print()
df2 = pd.DataFrame([word_dict.keys(), word_dict.values()])
print(df2)
df2 = df2.T
df2.columns = ['단어', '빈도수']
print(df2.head(5))

# ... 


