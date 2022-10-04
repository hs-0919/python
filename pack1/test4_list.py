# 묶음형(집힙형) 자료형 : list - 순서 o, 수정 가능
a= [1,2,3]; b=[10, a, 12.5,  True, '금쪽이']
print(a, type(a), id(a))
print(b, type(b), id(b))
aa =[]
bb= list()
print(type(aa), type(bb))
 
print()
family=['엄마','아빠','나','형']
print(family[2]) # 인덱싱
print(family[0:2])# 슬라이싱
family.append('단풍이') # 추가 - 맨뒤에 붙음
family.insert(0, '할아버지') # 삽입 - 0번째에 넣어라
family.extend(['외삼촌', '큰누나']) #추가
family += ['작은이모', '큰이모'] 
family.remove('단풍이') # remove는 밸류를 삭제 
del family[2] # del은 순서에 의한 삭제,  아빠 지워짐 - 2번째 지워짐
print(family, len(family))
print(family.index('나'))
print('엄마' in family, '할머니' in family) # 있는지 확인하는거 

del family # 변수를 삭제
#print(family)

print()
aa =[1,2,3,['a', 'kbs', 'c'],4,5] #중첩 list
print(aa)
print(aa[0])
print(aa[3])
print(aa[3][1]) # 3번째 꺼에서 1번째 꺼 - kbs만 나옴

print(id(aa))
aa[0] = 333 # 요소값 수정 가능
print(aa, id(aa))


print()
aa2=['123', '34', '234']
print(aa2)
aa2.sort() # 사전형식으로 정렬
print(aa2)
aa2.sort(key=int, reverse=True) # 문자를 숫자처럼 하고 가장 큰수부터 나열 
print(aa2)

print()
name=['소현', '금쪽이', '다정']
print(name)
name2 = name   # 얕은 복사 : 주소 치환 / 자바 와 파이썬은 소멸자가 없다 (일정시간이 지나면 메모리가 자동 소멸)
print(id(name), id(name2))

import copy
name3 =copy.deepcopy(name) # 깊은 복사. 새로운 객체로 생성

print(id(name), id(name2), id(name3))
name[0] = '용환'
print(name)
print(name2)
print(name3)

# 당장 몰라도 됨 참고임.. 알고 있어야한다 언젠간... -------------------------
print("stack, queue") #stack : LiFO(last),  queue : FiFO(first)
sbs=[1,2,3]
sbs.append(4)
print(sbs)
sbs.pop()
print(sbs)
sbs.pop()
print(sbs) #뒤에서 부터 빠져나감.

print()
sbs=[1,2,3]
sbs.append(4)
sbs.pop(0)
print(sbs)
sbs.pop(0)
print(sbs) #앞에서 부터 빠져나감.



