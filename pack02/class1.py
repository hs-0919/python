# class : 새로운 타입을 생성. 객체 지향적(중심적)인 프로그래밍
# 형식 class 클래스명(): 멤버(필드, 메소드) ~
# 생성자, 소멸자가 있다.
# 접근지정자가 없다. 
# 다중상속 가능, interface가 없다.

print('뭔가를 하다가 모듈의 멤버인 클래스를 선언하기')

class TestClass:    # prototype , 원형클래스 객체 생성. 고유의 이름 공간을 확보
    aa =1 # 멤버변수(멤버필드), public
    
    def __init__(self): # 생성자
        print('생성자')
        
    def __del__(self):
        print('소멸자')
        
    def printMessage(self): # method
        name= '한국인'  # 지역변수
        print(name)
        print(self.aa)
        
print(TestClass, id(TestClass))
print(TestClass.aa) # 1

print('****')
test = TestClass()  # 생성자를 호출한 후 TestClass type의 객체 생성, 생성자
print(test.aa)  # 멤버필드 호출, 1

# 메소드 호출
# TestClass.printMessage() => 에러뜸
test.printMessage() # 한국인, 1
TestClass.printMessage(test) # UnBound method call / 한국인, 1
print('-----')
test.printMessage()  # Bound method call / 한국인, 1

print()
print(type(1))
print(type(1.1))
print(type(test))
print(id(test), id(TestClass))
