# 기상청 제공 날씨정보 XML 자료 읽기

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data = urllib.request.urlopen(url).read()

soup = BeautifulSoup(data, 'html.parser')

#find method

title = soup.find('title').string
print(title)
# ![CDATA[]] -> html이 파씽(번역)하죠? ,, ~ cdata section안에 넣어주면 파싱하지 않는다~

wf = soup.find('wf').string
print(wf)

city = soup.find_all('city')
print(city)
cityData =[]
for c in city:
    cityData.append(c.string)
    
df = pd.DataFrame()
df['city'] = cityData
print(df.head(3), len(df))

print()
# select method
tempMins = soup.select('location > province + city + data > tmn') # province + city + data - next씨블링
tempData =[]
for t in tempMins:
    tempData.append(t.string)

df['temp_min'] = tempData
df.columns = ['지역','최저기온']
print(df.head(3))

df.to_csv('날씨.csv', index=False)
print()
df2 = pd.read_csv('날씨.csv')
print(df2.head(3))

print('------df 자료로 슬라이싱 ... ------ ')
# iloc 
print(df.iloc[0])

print(df.iloc[0:2, :])
print(df.iloc[0:2, 0:1])
print(df.iloc[0:2, 0:2])
print()
print(df['지역'][0:2])
print()
print(df['지역'][:2])

# loc - 라벨값 기반의 2차원 인덱싱
print(df.loc[1:3]) # 1행에서 3행 출력
print(df[1:4])
print(df.loc[[1,3]]) # 1행 3행/ df.loc[[1:3]] -x
print(df.loc[:, '지역'].head(2))
print()
print(df.loc[1:3, ['최저기온','지역']])
print(df.loc[:, '지역'][1:4])

print('---------')
df = df.astype({'최저기온':int})  # 형변환
print(df.info())
print(df['최저기온'].mean(), ' ', df['최저기온'].std())

print(df['최저기온'] >= 6) # 6도이상 도시 T, F 로 나타남
print(df.loc[df['최저기온'] >= 7]) # 7도 이상 도시

print(df.sort_values(['최저기온'], ascending=True))






