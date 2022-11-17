# 클래스 

class Car: 
    handle = 0  # Car type의 객체에서 참조 가능 멤버 필드
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def showData(self): # Car type의 객체에서 참조 가능 멤버 메소드
        km = '킬로미터'
        msg = '속도:' + str(self.speed) + km + ', 핸들은 ' + str(self.handle)
        return msg

print(id(Car))
print(Car.handle)
print(Car.speed)
print()
car1 = Car('tom', 10)   # 생성자 호출 후 객체 생성-> __init__ 으로
print(car1.handle, car1.name, car1.speed)
car1.color = '보라해'
print('car1 color : %s'%car1.color)

print('-------')
car2=Car('james', 20)
print(car2.handle, car2.name, car2.speed)
#print('car2 color : %s'%car2.color) #  err ->'Car' object has no attribute 'color'
print('주소 : ', id(Car), id(car1), id(car2))

print()
print(car1.showData())
print(car2.showData())  # 바운드 메소드 콜
print(Car.showData(car2))   # 언바운드 메소드 콜
print("------")
car2.speed = 100
Car.handle = 1
car1.handle = 2
print('car1 : ', car1.showData())  # 10
print('car2 : ', car2.showData())  # 100
print()

'''
Car의 설계도가 static에 있고
car1=Car('tom',10) 하면
car1이라는 변수가 stack 영역에 있는데 
car1이 heap 영역에 있는 Car('tom',10) 의 주소를 참조
'''
