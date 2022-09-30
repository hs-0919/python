'''
여러줄 주석
'''
"""
주석
"""
# 한줄 주석 - ctrl + / 누르면 한줄 주석


var1= '안녕'
print(var1)
var1=5
print(var1)
#변수 선언시 type을 선언하지 않음

print()
a=10
b=12.5
c=b 
print(a, '', b, '', c)
print('주소출력 :', id(a), '', id(b),'', id(c))
# b와 c 는 같은 주소를 가지고 있다. 절대 주소는 아니다, 해쉬주소(?) 
print(a is b, a==b) # 주소 비교, 값 비교
print(c is b, c==b)

aa = [1000]
bb = [1000]
print(aa == bb, aa is bb)
print(id(aa), '' , id(bb))

print('-------')
A=1; a=2; # 변수는 대소문자 구별함
print('A+a',A + a, id(A), id(a))

print()
import keyword
print('키워드(예약어)목록 : ', keyword.kwlist)
# 키워드는 변수로 설정 안된다. 오류난다...

print()
print(10, oct(10), hex(10), bin(10))
print(10, 0o12, 0xa, 0b1010) # 다 10이다.

print('자료형')
print(3, type(3))
print(3.4, type(3.4))
print(3 + 4j, type(3+4j))
print(True, type(True))
print("good", type('good'))

print((1,), type((1,)))#튜플 타입
print([1], type([1])) #리스트
print({1}, type({1})) #set 타입
print({'k':1}, type({'k':1})) #딕셔너리

print(isinstance(1, int)) #type을 확인하는 연산자.
print(isinstance(1.2, float))
