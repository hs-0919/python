from abc import *

class Employee(metaclass = ABCMeta):
    
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai= nai
        
    @abstractmethod
    def pay(self): #추상 메소드가 됨
        pass
    
    @abstractmethod
    def data_print(self):
        pass
        
    def irumnai_print(self):
        pass
    
print(' Temporary ')

class Temporary(Employee):
    def __init__(self, irum, nai , ilsu, ildang):
        self.ilsu = ilsu
        self.ildang = ildang
        Employee.__init__(self, irum, nai)
    
    def pay(self):
        return self.ilsu*self.ildang
        
    def data_print(self):
        print('이름 : {}, 나이 : {}, 월급 : {}'.format(self.irum, self.nai, str(self.pay())))

class Regular(Employee):
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai)
        self.salary = salary
        
    def pay(self):
        return self.salary
    
    def data_print(self):
        print('이름 : {}, 나이 : {}, 급여 : {}'.format(self.irum, self.nai, str(self.pay())))
        
        
class Salesman(Regular):
    def __init__(self, irum, nai, salary, sales, comission):
        super().__init__(irum, nai, salary)
        self.sales = sales
        self.comission = comission
    def pay(self):
        return super().pay() + (self.sales*self.comission)

    def data_print(self):
        print('이름 : {}, 나이 : {}, 수령액 : {}'.format(self.irum,self.nai,str(self.pay())))
     
t = Temporary('홍길동', 25, 20, 150000)
r = Regular('한국인', 27,3500000)
s = Salesman('손오공', 29,1200000, 50000000, 0.25)

t.data_print()
r.data_print()
s.data_print()