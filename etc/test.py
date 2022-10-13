'''
i=1
while i <= 10:
    j=1
    re=''
    while j<=i:
        re =re + '*'
        j += 1
    print(re)
    i += 1
'''
'''
a = int(input('연도 입력: '))
if a % 4 == 0 and not a % 100 == 0 or a % 400 == 0:
    print('%d 은 윤년'%a)
else:
    print('%d 은 평년'%a)
'''    
'''
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue         
    if i > 100:
        break 
                 
    print(i, end=' ')
    i += 1

try:
    aa = int(input())
    bb = 10 / aa 
    print(bb)

except ZeroDivisionError:
    print('에러 : 0으로 나누면 안됩니다')
'''
"""
from abc import *

class bicycle(metaclass = ABCMeta):
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def display(self):
        pass
    
class pay(bicycle):
    def __init__(self, name, wheel, price):
        bicycle.__init__(self, name)
        self.wheel = wheel
        self.price = price
        
    def bicyclePrice(self):
        return self.wheel*self.price
    
    def display(self):
        print('{}님 자전거 바퀴가격 총액은 {}원 입니다.'.format(self.name,str(self.bicyclePrice())))
    
gildong = pay('길동', 2, 50000) # name, wheel, price
gildong.display()
"""
print((lambda m,n: m + n * 5)(1,2))












