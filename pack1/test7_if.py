# 조건 판단문 if
# if 조건 : 실행문 elif 조건 ~ else : ~

var =1
if var >= 3:        #java : {}, py : 들여쓰기
    print('크구나')
    print('참일 때')
    # pass  아무것도 수행 하지 않음.
else:
    print('거짓일 때')    

print('end1')

print()
money= 1000
age= 35

if money >= 500:
    item ='사과'
    if age <= 30:
        msg ='청춘이다'
    else:
        msg ='라떼는 말야...'
else:
    item ='포도'
    if age >= 30:
        msg ='성인이다'
    else:
        msg ='잼민이다'
print(item, msg)
        
print()
jumsu = 85
if jumsu >= 90:
    print('우수')
else:
    if jumsu >= 70:
        print('보통')
    else:
        print('망')
        
print()
if jumsu >= 90:
    print('우수')
elif jumsu >= 70:
    print('보통')
else:
    print('망')

print()
print(int('5')+5) # 형변환 : int(), str()
print(str(5)+'5')

#jum = int(input('점수 입력:'))
jum =80
# print(jum, type(jum))
#if jum >= 90 and jum <=100:

if 90 <= jum <= 100:
    grade='우수학생'
elif 70 <= jum <90:
    grade ='보통학생'
else:
    grade ='저조학생'
print(grade)

print()
names =['홍길동', '신기해', '이기자']
if '홍길동' in names: # not in - 부정, 부정문 좋지 않음 -속도가 떨어짐
    print('친구 이름')
else:
    print('누구니?')

print()
a = 'kbs'
b = 9 if a == 'kbs' else 11 # 이런식으로 많이 사용한다.
print(b)

a = 11
b = 'mbc' if a == 9 else 'kbs'
print(b)

print()
a = 3 
if a <5:
    print(0)
elif a<10:
    print(1)
else:
    print(2)

print(0 if a < 5 else 1 if a <10 else 2)

print(a * 2 if a > 5 else a + 2 )
        
print((a+2, a*2)[a >5]) # [a >5] -> false 라서 a+2 실행, true면 a*2 실행 

