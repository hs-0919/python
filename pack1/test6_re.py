# 정규 표현식 : 다량의 데이터에서 원하는 데이터만 선택해서 처리할 때 효과적

import re

ss ="12_1234 abc가나다abc_nbc_ABC_1234555_6한국Python is fun."
print(ss)
print(re.findall(r'123', ss)) # r을 쓰는게 좋다.
print(re.findall(r'가나다', ss))
print(re.findall(r'1', ss))
print(re.findall(r'[1-2]', ss))
print(re.findall(r'[0-9]', ss)) #정규표현식에선 띄어쓰기 하면안됨.
print(re.findall(r'[0-9]+', ss))
print(re.findall(r'[0-9]{2}', ss)) # {} - 횟수 반복(?)
print(re.findall(r'[0-9]{2,3}', ss))#2개짜리~ 3개짜리
print(re.findall(r'[a-z]+', ss))
print(re.findall(r'[A-Za-z]+', ss)) # + - 한개 이상, * - 0개 이상, ? - 0 또는 1
print(re.findall(r'[가-힣]+', ss))
print(re.findall(r'[^가-힣]+', ss)) # ^ - 부정 
print(re.findall(r'12|34', ss))
print(re.findall(r'.bc', ss)) # . - 아무거나
print(re.findall(r'...', ss)) # ... - 세글자 아무거나
print(re.findall(r'[^1]+', ss)) # 부정
print(re.findall(r'^1+', ss)) # 첫글자 1
print(re.findall(r'fun.$', ss)) # $ 끝나는거 

print(re.findall(r'\d', ss)) # 숫자만 나옴
print(re.findall(r'\d+', ss))# 그룹이 된다.
print(re.findall(r'\s', ss))
print(re.findall(r'\S', ss))
print(re.findall(r'\d{1,3}', ss)) # 1~3 까지

print()
p=re.compile('the', re.IGNORECASE)
print(p)
print(p.findall('The do the dog'))
print()

ss='''My name is tom.
I am happy'''
print(ss)
p=re.compile('^.+',re.MULTILINE)
print(p.findall(ss))






