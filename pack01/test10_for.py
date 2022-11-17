# 반복문 for 
# for 변수 in 집합형 자료:...


#for i in [1,2,3,4,5]: # list
#for i in (1,2,3,4,5): # 튜플
for i in {1,2,3,4,5}: # set
    print(i, end=' ')    
print()
soft ={'java':'웹영언어', 'python':'만능언어', 'MariaDB':'데이터 처리'}
print(soft.items()) #dict_items([('java', '웹영언어'), ('python', '만능언어'), ('MariaDB', '데이터 처리')])

for i in soft.items():
    #print(i) # 튜플만 보임
    print(i[0] + '^^;' + i[1])

print()
for k in soft.keys():
    print(k, end=' ')
    
print()
for k in soft.values():
    print(k, end=' ')

print()
li = ['a','b','c']
for idx, data in enumerate(li): # enumerate() - index를 반환함
    print(idx, data)
    
print('\n평균, 분산, 표준편차 구하기') # 평균이란... 검색해보기
jum = [1,3,5,7,9]
print(jum)

tot =0
for i in jum:
    tot +=i
    
avg =tot/len(jum)
print('mean : ', avg)

tot= 0
for i in jum:
    tot += (i - avg) ** 2  # (i - avg)-편차
    
var = tot/len(jum)
print('var : ', var) # 분산은 편차 제곱합의 평균
import math
print('std : ', math.sqrt(var)) # 표준편차 # = print('std : ', var ** 0.5)

print('----------------------')

for n in [2,3]:
    print('---{}단---'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{}*{}={}'.format(n, i, n*i))
    print()
    
print()
datas =[1,2,3,4,5]
for i in datas:
    if i ==3: continue
    if i ==4: break
    print(i, end=' ')
else:
    print('정상 종료 일때 수행')

print()
jumsu = [95, 73, 87, 80, 100, 50]
number = 0 
for jum in jumsu:
    number += 1
    if jum < 70:continue
    print('%d번째 수험생은 합격입니다.'%number)
    
print()
li1 =[3,4,5]
li2 =[0.5, 1,2]
result =[]
for a in li1: 
    for b in li2:
        print(a+b, end=' ')
        result.append(a+b)
print(result)

datas = [a + b for a in li1 for b in li2]
print(datas)

print('\n다량의 문자열 데이터 중 단어 수 출력')
import re
ss = '''
5일 코로나19 신규확진자 수가 3만4739명을 기록했다. 전일보다 1420명 줄었다. 
위중증 환자와 사망자 등 방역 관련 모든 지표가 안정세다. 
이제 방역 관건은 코로나19 자체보다 독감이라는 말이 의료계에서 나온다.
3년만에 독감 유행이 예고됐으며 독감과 코로나19가 동시 유행할 경우 환자 중증도가 크게 올라갈 우려가 있어서다.
게다가 올해 유행할 독감은 독감 바이러스 중에서도 가장 강한 'A형 H3N2'다. 
적극적 독감백신 접종이 필요하다는 것이 방역당국과 의료계 공통된 의견이다.
중앙방역대책본부는 이날 0시 기준 신규확진자 수가 3만4739명을 기록했다고 밝혔다. 
이 가운데 해외 유입사례 69명을 제외한 국내 확진자 수는3만4670명이었다. 
수도권에서 전체 국내 확진의 56.5% 비중인 1만9587명이 확진됐다. 
재원중 위중증 환자는 330명으로 전일대비 20명 감소했다. 
사망자는 16명으로 전일보다 3명 줄었다. 누적 사망자는 2만8544명(치명률 0.11%)이다.
'''
print(ss)
print()
ss2 = re.sub(r'[^가-힣\s]', '', ss)
print(ss2)
ss3 = ss2.split(' ')
print(ss3)

cou={} # 단어의 발생 횟수를 dict 로 저장
for i in ss3:
    if i in cou:
        cou[i]+=1
    else:
        cou[i]=1
print(cou)
    
print()
for test_str in ['111-1234', '일이삼-사오육칠', '222-1234']:
    if re.match(r'^\d{3,4}-\d{4}$',test_str):
        print(test_str, '전화번호 맞아요')
    else:
        print(test_str, '음...')
    
print(sum([1,2,3]))

print('사전형 사료로 과일값 출력')
price ={'사과':2000, '감':500, '배':1000}
guest ={'사과':2, '감':3}
bill = sum(price[f] * guest[f] for f in guest)
print('고갱님이 구매한 과일 총액 : {}원'.format(bill))

print('---------------------')
temp =[1,2,3]
for i in temp :
    print(i, end=' ')
print()
print([i for i in temp])
print({i for i in temp})

temp2 = list()
for i in temp:
    temp2.append(i + 10)
print(temp2)
temp2 =[i+10 for i in temp]
print(temp2)

print()
datas =[1,2,'a', True, 3]
li =[i * i for i in datas if type(i) == int]
print(li)

print()
datas = {1,1,2,2,2,3}
se = {i*i for i in datas} # set type 이라 중복을 제거
print(se)

print()
id_name = {1:'tom', 2:'james'}
name_id ={value:key for key, value in id_name.items()}
print(name_id)
