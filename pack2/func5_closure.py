# 클로저(closure) : scope에 제약을 받지않는 변수를 포함하고 있는 코드 블록이다.
# 내부함수의 주소를 반환함으로 해서 함수내의 지역변수를 함수 밖에서 참조 가능 


def funcTimes(a,b):
    c =a*b
    return c 
print(funcTimes(2,3))

kbs = funcTimes(2, 3)
print(kbs)
kbs = funcTimes
print(kbs)
print(kbs(2, 3))
print(id(kbs), id(funcTimes))

del funcTimes
# funcTimes()
print(kbs(2,3))

mbc = sbs = kbs
print(mbc(2,3))

# ----------------------

print('클로저를 사용하지 않은 경우 ----')

def out():
    count=0
    def inn():
        nonlocal count
        count += 1 # err 발생 - 
        return count
    # print(inn())
    imsi = inn()
    return imsi

#out()
#print(count) #err 발생
#out()
print(out())
print(out())
print(out())

print('클로저를 사용한 경우 ----------')

def outer():
    count=0
    def inner():
        nonlocal count
        count += 1 
        # ...
        return count
    return inner  # <===== 이게 클로저이다. : 내부함수의 주소를 반환

var1 = outer()
print(var1) # inner 주소를 가지고 있다.
print(var1()) # inner 가 count를 가지고 있어 1이 찍힌다.
print(var1()) # count += 1 => 2
print(var1()) # count += 1 => 3
print(var1()) # count += 1 => 4

print('*** 수량 * 단가 *세금을 계산하는 함수 만들기')
# 분기별로 세금은 동적이다.
def outer2(tax): # tax는 - local 변수 이다 / 함수에서 선언하면 로컬 변수이다
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2 # <===== 이게 클로저이다. : 내부함수의 주소를 반환 

# 1분기에는 tax가 0.1(10%) 부과, 
q1 = outer2(0.1) # q1은 inner2의 주소를 기억하고 있다.
result1 = q1(5, 50000)
print('result1 : ', result1)
result2 = q1(1, 10000)
print('result2 : ', result2)

# 2분기에는 tax가 0.05(5%) 부과, 
q2 = outer2(0.05) # q1은 inner2의 주소를 기억하고 있다.
result3 = q2(5, 50000)
print('result3 : ', result3)
result4 = q2(1, 10000)
print('result4 : ', result4)








