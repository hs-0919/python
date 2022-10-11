# 다중 상속 : 순서가 중요

class Tiger:
    data = '호랑이 세상'
    
    def cry(self):
        print('호랑이는 어흥')
        
    def eat(self):
        print('맹수는 고기를 좋아함.')
        
class Lion:
    def cry(self):
        print('사자는 으르렁')
        
    def hobby(self):
        print('백수의 왕은 낮잠을 즐김')
        
class Liger1(Tiger, Lion):  # 다중 상속
    pass

a1 = Liger1()
a1.cry()        
a1.eat()
a1.hobby()
print(a1.data)
        
print('----------')
class Liger2(Lion, Tiger):
    data = '라이거 만세'
    
    def hobby(self):
        print('라이거는 자바를 싫어해')
    def showData(self):
        print(self.data, ' ', super().data)
        self.hobby()
        super().hobby()
        
        
        
a2 = Liger2()
a2.cry()
a2.eat()
a2.hobby() # 우선순위가 있다.
a2.showData()
      
        
        
        