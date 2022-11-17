# method override(재정의)

class Parent:
    def printData(self):
        pass
    
class Child1(Parent):
    def printData(self):    # method override
        print('Child1에서 재정의')
        
        
class Child2(Parent):
    def printData(self):    # method override
        print('Child2에서 재정의')        
        print('오버라이드는 부모의 메소드를 자식이 재정의')
        
    def abc(self):
        print('Child2 고유 메소드')
    
    
c1 = Child1()
c1.printData()

print()

c2 = Child2()
c2.printData()

print('다형성 -----')
par = Parent()
par = c1
par.printData()
print()
par = c2
par.printData()
par.abc()

print()
plist =[c1,c2]
for i in plist:
    i.printData()

