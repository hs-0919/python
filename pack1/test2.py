#연산자, 출력 서식 

v1=2 #치환
v1=v2=v3=v4=5
print(v1,v2,v3,v4)

v1=1,2,3
print(v1)

v1,v2=10,20
print(v1,v2)
v2,v1=v1,v2
print(v1, v2)

print('값 할당 packing')
# v1,v2 = 1,2,3,4,5
*v1,v2 = 1,2,3,4,5
v1,*v2 = 1,2,3,4,5
#*v1,*v2 = 1,2,3,4,5 -  에러가 발생한다.
print(v1)
print(v2)

*v1,v2,v3=1,2,3,4,5
print(v1,v2,v3)

print()
print('------------')
print('\n연산자(산술, 관계, 논리)')
print(5+3,5-3,5*3,5/3)
print(5 //5, 5%3, divmod(5,3))#몫 과 나누기


print('연산자 우선순위', 3+4*5, (3+4)*5)
# 소괄호 () > 산술 연산자(**거듭제곱 > *,/ > +, -) > 관리연산자 > 논리연산자 > 치환(=)

print('관계연산자')
print(5>3, 5==3, 5 != 3)
print('논리연산자')
print(5>3 and 4<3, 5>3 or 4<3, not(5>=3))

print('문자열 더하기 연산자')
print('파이썬'+'만'+'세')
print('파이썬'*10)

print('누적')
a=10
a= a+1
a += 1
#a++ 증감연산자 X a--
print('a:', a)

print()
print(a, a* -1, -a, --a)
#파이썬은 증감연산자가 없다.

print('bool :', True, False, type(True))
print(bool(True), bool(1), bool(-23.4), bool('kbs'))
print(bool(False), bool(0), bool(''), bool(None), bool([]),bool(()),bool({}))

print('***' * 10);
# 츨력 서식
print(format(123.45678, '10.3f')) #전체 10자리 확보하고 앞에 3자리 공백, 4번째 자리에서 반올림 하기
print(format(123.45678, '10.3'))
print(format(123, '10d')) 
print ('{0:.3f}'.format(1.0/3))#소수 세번째자리 까지
print ('{0:_^11}'.format('hello'))
print ('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# 많이 사용함.
print('이름:{0}, 가격:{1}'.format('마우스', 5000))
print('이름:{0}, 가격:{1}'.format('마우스', 5000))# 인덱스를 쓰지않아도 순서대로 들어옴
print('이름:{1}, 가격:{0}'.format('마우스', 5000))
print('이름:{1}, 가격:{0}, 가격:{0} '.format('마우스', 5000))

# 많이 사용함.
print('나는 나이가 %d 이다.'%23) 
print('나는 나이가 %s 이다.'%'스물셋')# 문자
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100)) #실수 ,%f-소수6자리 정해짐.

print('~~~' * 10)
print('aa\tbb') # \t - tab키
print(r'aa\tbb')# 앞에 raw string(r)을 선행하면 이스케이프(\) 기능 해제 
print("c:\aa\abc\nbc.txt")
print(r"c:\aa\abc\nbc.txt")# 앞에 raw string(r)을 선행하면 이스케이프(\) 기능 해제 

print('aa', end=', ') #print 는 기본적으로 라인스킵이 있다. end='' 를 사용하면 라인스킵이 안됨.
print('bb')



