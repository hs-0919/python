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

