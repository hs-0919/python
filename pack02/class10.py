# 클래스의 상속 

class Person:
    say = '난 사람'
    age = '29'
    __kbs = '공영방송' # private 멤버변수 - person 클래스에서만 유효하다.
    
    def __init__(self, age):
        print('Person 생성자')
        self.age = age      #
    
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.age, self.say))
            
    def hello(self):
        print('안녕', self.__kbs)

print(Person.say, Person.age)
# Person.printInfo -> 이렇게는 쓸 수 없다. 
p = Person('26') # -> def __init__(self, age) 일로 넘어옴
p.printInfo()
p.hello()

print('***'*10)
'''
class Employee(Person):
    pass
emp= Employee('27') # 부모 생성자가 실행되어서 - age 인자가 필요함
emp.printInfo()
'''
class Employee(Person):
    say = '일하는 동물'
    subject = '근로자'
    
    def __init__(self):  
        print('Employee 생성자')
        
    def printInfo(self):
        print('Employee의 printInfo메소드')
        
    def empPrintInfo(self):
        print(self.say, self.age, self.subject)    
        print(self.say, super().say, super().age) # super(). ->  바로 부모 생성자로 올라감
        self.printInfo() # -> 현재 클래스 부터 뒤짐
        super().printInfo() # -> 바로 부모 클래스로 올라가 뒤짐
        self.hello()
        # print(super().say, super().__kbs) -> 에러남, super().__kbs-> person 클래스에서만 유효
        
        
emp= Employee() # def __init__(self) -> 인자를 하나 더 받으면 에러가 남..
emp.printInfo()
emp.empPrintInfo()

print('***'*10)
class Worker(Person):
    def __init__(self, age):
        print('Worker 생성자')
        super().__init__(age)   # 부모 생성자 호출 - 바운드 메소드 콜

    def wprintInfo(self):
        self.printInfo()
        
wor = Worker('24')
print(wor.say, wor.age)
wor.wprintInfo()

print('***'*10)
class Programmer(Worker):
    def __init__(self, age):
        print('Programmer 생성자')
        # super().__init__(age)    # Bound call
        Worker.__init__(self, age) # UnBound call
    
    def ProShow(self):
        self.printInfo()
    
    
pr = Programmer('내년 30')
print(pr.say, pr.age)
pr.ProShow()


print('~~~~~~~~~~~~~~~~~~~')
print(type(3))
print(type(pr))
print(type(wor))
print(Programmer.__bases__, Worker.__bases__, Person.__bases__)






