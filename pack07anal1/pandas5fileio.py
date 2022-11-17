# pandas로 파일 찾기 및 저장

import pandas as pd
from _csv import writer

df = pd.read_csv("../testdata/ex1.csv")
print(df, type(df))
print()
df = pd.read_table("../testdata/ex1.csv", sep=',')
print(df)
print()
df = pd.read_csv("../testdata/ex2.csv", header=None, names=list('korea'))
print(df)

print()
df = pd.read_csv("../testdata/ex3.txt")
print(df)
print(df.describe())
print()
df = pd.read_table("../testdata/ex3.txt", sep=' ') # sep - 구분자, 공백
print(df)
print(df.describe())
print()
df = pd.read_table("../testdata/ex3.txt", sep='\s+') # 정규표현식
print(df)
print(df.describe())
print()
df = pd.read_table("../testdata/ex3.txt", sep='\s+', skiprows=[1,3])
print(df)
print(df.describe())

print() # 자리수로 끊어읽기
df = pd.read_fwf("../testdata/data_fwt.txt", head=None, widths=(10,3,5), names=('date', 'name', 'price'))
print(df)
print(df['date'].head(3))

print('chunk : 파일의 크기가 큰 경우 일정 행 단위로 끊어 읽기')
test = pd.read_csv("../testdata/data_csv2.csv", header=None, chunksize=3)
print(test)

print('------------')
for piece in test:
    print(piece.sort_values(by=2, ascending=True))  # 2번째 열 내림차순 정렬(청크 단위)
    
print()
print('Series / DataFrame을 파일로 저장----')
items = {'apple':{'count':10, 'price':1500}, 'orange':{'count':5, 'price':1000}}
df = pd.DataFrame(items)
print(df)

df.to_clipboard()
print(df.to_html())
print(df.to_csv())
print(df.to_json())
df.to_csv('result1.csv')
df.to_csv('result2.csv', index=False, sep=',')
df.to_csv('result3.csv', index=False, header=False, sep=',')

data= df.T
print(data)
data.to_csv('result4.csv', index=False, sep=',')

print('excel파일로 저장/읽기')
print(df)
writer = pd.ExcelWriter('result5.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='testSheet')
writer.save()

print()
myexcel = pd.read_excel('result5.xlsx', sheet_name='testSheet')
print(myexcel) 











