# 클래스의 상속 : 다형성을 구사 가능

class Animal: 
    def __init__(self):
        print('Animal 생성자')
        
    def move(self):
        print('움직이는 동물 고양이 - 단풍이')
        
class Dog(Animal):  # 상속
    def __init__(self):   # 자식의 생성자가 있을때 부모생성자 호출 x, 자식 생성자만 호출 o 
        print('Dog 생성자') # 부모 생성자는 따로 명시 해야한다. 
        
    def my(self):
        print('난 강아지~')
        

dog1 = Dog()  
dog1.move()
dog1.my()        
    
print()
class Horse(Animal):
    pass 

horse1 = Horse()
horse1.move()
    
