# 추상 클래스(추상 메소드) - 자식 클래스에서 부모의 메소드의 이름을 강요하도록 함

from abc import * 

class AbstractClass(metaclass = ABCMeta): # 추상 클래스가 됨.
    
    @abstractmethod
    def myMethod(self): # 추상 메소드가 됨
        pass
    
    def normalMethod(self):
        print('추상 클래스는 일반메소드를 가질 수 있다.')
    
# parent = AbstractClass() # err - Can't instantiate abstract class

class Child1(AbstractClass):
    name = '난 Child1'
    
    def myMethod(self):
        print('Child1에서 추상 메소드에 내용을 적용')
        
c1 = Child1()
print(c1.name)
c1.myMethod()
c1.normalMethod()



print()
class Child2(AbstractClass):
    def myMethod(self):
        print('Child2에서 추상의 마법을 풀다')
        print('이제는 자유다')
        
    def normalMethod(self):
        print('추상 클래스의 일반 메소는 오버라이딩이 선택적이다.')

    def good(self):
        print('Child2 고유 메소드')

c2 = Child2()
c2.myMethod()
c2.normalMethod()
c2.good()

print('---------------------')

imsi = c1
imsi.myMethod()
print()
imsi = c2
imsi.myMethod()









