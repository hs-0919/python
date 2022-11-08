# 함수 장식장 (decorator : @ - meta 기능이 있다.)
# 장식자는 또 다른 함수를 감싼 함수다. 주함수가 호출 되면 그의 반환값이 장식자에게 건네진다.
# 그러면 장식자는 포장된 함수로 교체하여 함수를 돌려 준다.


def make2(fn):
    return lambda: '안녕' + fn() # lambda function 의 주소를 리턴

def make1(fn):
    return lambda: '반가워 ' + fn()

def hello():
    return '홍길동'

hi = make2(make1(hello))
print(hi())
print()

@make2
@make1
def hello2():
    return '고길동'
print(hello2()) 

