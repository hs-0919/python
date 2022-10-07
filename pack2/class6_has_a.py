# 내장고에 음식 담기 - 클래스의 포함관계로 구현


class Fridge:
    isOpened = False
    foods = []
    
    def open(self):
        self.isOpened =True
        print('냉장고 문 열기')
        
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing) # 포함관계
            print('냉장고 안에 음식을 저장함.')
            self.food_list()
        else:
            print('냉장고 문이 닫쳐 있어 음식을 저장할 수 없다.')
    
    def close(self):
        self.isOpened = False
        print("냉장고 문 닫기")
    
    
    
    def food_list(self):
        for f in self.foods:
            print('-', f.name, f.expiry_date)
        print()

class FoodData:
    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date

if __name__ == '__main__':
    f = Fridge()
    
    apple = FoodData('사과', '2022-10-25')
    f.put(apple)
    f.open()
    f.put(apple)
    f.close()
    print()
    minfe=FoodData('민철','2088-11-11')
    f.open()
    f.put(minfe)
    f.close()



