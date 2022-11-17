#묶음형 자료형  

# tuple - list와 유사하나 읽기 전용. 순서O, 수정 불가

t = ('a', 'b', 'c', 'a')
#t = 'a', 'b', 'c', 'a' 
print(t, type(t),len(t), t.count('a'), t.index('b'))

print(t[0])
#t[0] = 'k' # 'tuple' object does not support item assignment - 수정 불가

imsi =list(t)
print(imsi, type(imsi))
imsi[0] = 'k'
t = tuple(imsi)
print(t)

print()
print((1), type((1)))
print((1,), type((1,))) # ,를 찍어야 튜플로 인정된다(반드시).

print()
t1=(10,20)
a, b = t1
b, a = a, b
t2 =a,b
print(t2)



print('----------set-----------')
# set - 순서가 없다, 중복이 불가하다! (순서X, 중복X)
a={1,2,3,1}
print(a, type(a), len(a))

b={3,4}

print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a-b)   # 차집합
print(a | b) # 합집합
print(a & b) # 교집합

print()
print(a)
#print(a[0]) -> err 순서가 없기 때문에 에러발생
#a[0]=100 -> 'set' object does not support item assignment - set은 순서가 없다

a.update({4,5}) # .update함수를 통해 수정이(추가) 가능함.
a.update([6,7,8])
a.update((9,))
print(a)

a.discard(3) # 값에 의한 삭제(순서에 의한 삭제는 없다)
a.remove(5)  # 값에 의한 삭제
a.discard(3) # 값에 의한 삭제 - 해당 값이 없으면 통과한다.
#a.remove(5) # 값에 의한 삭제 - 해당 값이 없으면 에러가 발생한다.
print(a)

c=set()
c=a
print(c)
a.clear() # 날리는거
print(a)
print(c)

print()
li=[1,2,3,1,2,3]
print(li)
imsi=set(li) # 중복 배제
li=list(imsi) 
print(li)

print('----------dict-----------')
# 사전형 : {'key':'value'} - 순서X, key를 이용해 value를 참조, JSON과 잘맞음

my = dict(k1=1,k2='mbc', k3=3.4)
print(my, type(my))

dic={'파이썬':'뱀', '자바':'커피', '스프링':'용수철', '점수':[60,70,80]}
print(dic, type(dic), len(dic))
print(dic['자바'])
#print(dic[0])  -> 순서가 없어서 err발생

dic['오라클']='예언자' # 추가 가능함
print(dic)

del dic['오라클'] # 삭제
dic.pop('파이썬')
print(dic)

dic['자바']='웹용언어' # 수정이 가능
print(dic)

print(dic.keys())
print(dic.values())
print('파이썬' in dic)



'''
str : 순서O, 수정X
list: 순서O, 수정O []
tuple:순서O, 수정X ()
set : 순서X, 수정X, 중복X {}
dict: 순서X, 키에 의한 value 참조 {:}
'''


