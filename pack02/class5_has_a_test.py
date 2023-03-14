'''
class coffeeMachine:
    def showData(self, cupCount, change):
        print('커피 %d잔과'%cupCount, '잔돈 %d원'%change)

class coinIn:
    coffeePrice=200
    
    def __init__(self):
        self.data = coffeeMachine() # 클래스의 포함
    def culc(self):
        
        coin=int(input('동전을 넣으세요 : '))
        if coin == 200:
            self.data().showData(1, 0)
        elif coin == 400:
            self.data().showData(2, 0)
        else:
            print('요금이 부족합니다.')  

if __name__ == '__main__':
    coinIn().culc() 
'''

# 왕자님꺼 
class CoinIn:
    
    def insert(self):
        self.coin=int(input('동전을 넣어주세요'))
        return self.coin
class Machine:
    
    def showData(self):
        
        print('커피는 한잔에 200원 입니다')
        self.coin=CoinIn().insert()
        self.count=int(input('몇잔을 원하세요?'))
        
        if 200*self.count > self.coin:
            print('요금이 부족합니다')
        elif 200*self.count <= self.coin:
            refund=self.coin-(200*self.count)
            print('커피 %d잔과'%self.count,'잔돈 %d원'%refund)
        
if __name__=='__main__':
    Machine().showData()

# 클래스의 포함관계 연습문제  - 선생님꺼
'''
class CoinIn:
    def calc(self, cupCount):
        re = ""
        
        if self.coin < 200:
            re = "요금이 부족하네요"
        elif cupCount * 200 > self.coin:
            re = "요금이 부족하네요"
        else:
            self.change = self.coin - (200 * cupCount)  # 잔돈 계산
            re = "커피 {}잔과 잔돈 {}원".format(cupCount, self.change)

        return re

class Machine():
    cupCount = 1  # 현재 코드에서는 의미 없음

    def __init__(self):
        self.coinIn = CoinIn()  # 포함

    def showData(self):
        self.coinIn.coin = int(input("동전을 입력하세요 :"))
        self.cupCount = int(input("몇 잔을 원하세요 :"))

        print(self.coinIn.calc(self.cupCount))


if __name__ == '__main__':
    Machine().showData()
'''
            
            
            
        