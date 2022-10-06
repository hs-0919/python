# 함수 : argument와 parameter 키워드로 matching 하기
# 매개변수 유형
# 위치 매개변수 : 인수와 순서대로 대응 
# 기본값 매개변수 : 매개변수에 입력값이 없으면 기본값 사용
# 키워드 매개변수 : 인수와 매개변수를 동일 이름으로 대응
# 가변 매개변수 : 인수의 갯수가 동적인 경우


def showGugu(start, end=5):
    for dan in range(start, end+1):
        print(str(dan)+'단 출력')

showGugu(2,3)
print()
showGugu(3)
print()
showGugu(start=2, end=3)
print()
showGugu(end=3, start=2) # 서로 바뀌어도 똑같이 출력, 이름따라 간다.
print()
showGugu(2, end=3) # 이렇게 써도 결과는 같다
print()
# showGugu(start=2, 3) # 이건 에러가 발생한다.
print()
# showGugu(end=3, start=2) # 이것도 에러가 발생 , @@2두번째 인수를 상수로 주면 에러가 발생한다.@@

print('\n가변인수 처리')
def func1(*ar):
    #print(ar)
    for i in ar:
        print('밥 : '+i)

print()
func1('비빔밥', '공기밥 하나요')
func1('비빔밥', '공기밥 하나요','김치 더주세요')


def func2(a, *ar):
#def func2(*ar, a): # 에러 발생, 패킹 연산자는 앞에다 적으면 에러발생, 뒤에다 적어야 한다.
    print(a)
    for i in ar:
        print('밥 : '+i)

print()
func2('비빔밥', '공기밥 하나요')
func2('비빔밥', '공기밥 하나요','김치 더주세요')

print()
def calcProcess(op, *ar):
    if op == 'sum':
        re = 0
        for i in ar:
            re += i
            
    elif op == 'mul':
        re = 1
        for i in ar:
            re *= i
    return re

print(calcProcess('sum', 1,2,3,4,5))
print(calcProcess('mul', 1,2,3,4,5))

print()
def func3(w, h, **other): # ** - db연동할때 많이 사용한다 기억해야 한다.
    print('w:{}, h:{}'.format(w, h))
    print(other)
    
func3(55, 160)
func3(55, 160, name='홍길동') # {} dict 로 넣으면 안된다.{name='홍길동'}-err
func3(55, 160, name='홍길동', age=23)

print()
def func4(a,b,*c,**d):
    print(a,b)
    print(c)
    print(d)
func4(1,2)
func4(1,2,3) # 데이터하나 있을때 (3,) 튜플이고 콤마가 있다.(?)
func4(1,2,3,4,5)
func4(1,2,3,4,5, x=6,y=7) # **d -> {'x': 6, 'y': 7} 이런 모습으로 나옴....












