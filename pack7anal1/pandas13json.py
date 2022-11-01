# web 에서 JSON 문서읽기
import json
import urllib.request as req


url ="https://raw.githubusercontent.com/pykwon/python/master/seoullibtime5.json"
plainText = req.urlopen(url).read().decode()
print(type(plainText)) # <class 'str'>

jsonData = json.loads(plainText)  # str --> dict : json 디코딩
print(type(jsonData))  # <class 'dict'>

print(jsonData['SeoulLibraryTime']['row'][0]['LBRRY_NAME'])

print()
libDatas = jsonData.get('SeoulLibraryTime').get('row')
print(libDatas)

print()
datas =[]
for ele in libDatas:
    name = ele.get('LBRRY_NAME')
    tel  = ele.get('TEL_NO')
    addr = ele.get('ADRES')
    # print(name + '\t' + tel + '\t' + addr)
    imsi = [name, tel, addr]
    datas.append(imsi)

import pandas as pd
df = pd.DataFrame(datas, columns=['이름', '전화', '주소'])
print(df)
print(df.to_html())



