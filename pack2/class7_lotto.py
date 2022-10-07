# 클래스의 포함관계 : 로또번호 출력기 

import random

class LottoBall:
    def __init__(self, num):
        self.num = num

class Lottomachine:
    def __init__(self):
        self.ballList =[]
        for i in range(1, 46):
            self.ballList.append(LottoBall(i)) #포함 관계
    
    def selectBalls(self):
        # 볼 섞기 전 출력하기
        for a in range(45):
            print(self.ballList[a].num, end=' ')
        random.shuffle(self.ballList)   # 랜덤하게 공을 섞기 
        print()
        for a in range(45):
            print(self.ballList[a].num, end=' ')
        return self.ballList[0:6]
        
        
        
    
print()
class LottoUi:
    def __init__(self):
        self.machine = Lottomachine() # 포함
        
    def playLotto(self):
        input('로또를 시작 하려면 엔터키를 누르세요!')
        selectedBalls = self.machine.selectBalls()
        print('당첨번호')
        for ball in selectedBalls:
            print('%d '%ball.num, end=' ')
            
            
if __name__ == '__main__':
    #lo = LottoUi()
    #lo.playLotto()
    LottoUi().playLotto()
    
    
    
    
    
    