# 함수 만들기
# def 함수명(매개변수, ....): ~~


print('뭔가를 하다가...')

def DoFunc1():   # 함수의 생성
    print('DoFunc1 수행')
    # return None # 생략
    

    

print('뭔가를 하다가 2...')   
DoFunc1() # 함수 호출
print('뭔가를 하다가 2...')  
DoFunc1() # 함수 호출

print(DoFunc1)  # 파이썬은 대,소문자 구애받지 않는다.
DoFunc2 = DoFunc1  # 주소 치환
DoFunc2()

print(DoFunc1()) # 함수문을 수행하면 리턴값이 반드시 있다. 기본 None 리턴

print()

def DoFunc3(para1, para2):
   # pass    
   result = para1 + para2
   # print(result)
   return result
print(DoFunc3(10, 20))
aa = DoFunc3(10, 20)    
print(aa)
print(id(DoFunc3), DoFunc3, DoFunc3(1,2))
print('현재 파일(모듈)이 사용중인 객체 목록 : ', globals())

print(DoFunc3('대한', '민국'))
# print(DoFunc3('대한', 2)) # Type Error - 타입이 안맞아서
# print(DoFunc3(1)) # Missing Error - 1개만 써서
# print(DoFunc3(1,2,3)) # Missing Error - 2개인데 3개 써서

print('-----------')
def DoFunc4(arg1, arg2):
    if (arg1 + arg2) % 2 == 1:
        return
    else:
        aa =DoFunc5(arg1, arg2) # 함수 내에서 다른 함수 호출
        print(aa)


def DoFunc5(arg1, arg2):
    return arg1 + arg2

DoFunc4(5,6)
DoFunc4(5,5)

print()
def swapfunc(a,b):
    return b,a  # 하나 리턴함, 두개처럼 보이지만 한개를 리턴한다
                # tuple type 으로 묶여 하나의 값으로 반환
    # return (b,a)
    # return [b,a]

a=10; b=20;
print(swapfunc(a,b)) # 반환값 - tuple

print()
def func1():
    print('func1 함수 멤버')
    def func2():
        print('func1의 내부 함수인 func2 멤버')
    func2()
func1()

print()
# if 조건식 안에 함수 사용
def isOdd(para):
    return para % 2 == 1 
print(isOdd(5))
print(isOdd(6))
print(isOdd(7))

mydict = {x:x*x for x in range(11) if isOdd(x)}
print(mydict)

print('함수 연습용 게임 --- ')
import random
import time

def gameStart():
    print('보물을 찾아 여행을 떠나자. 동굴 문은 두개다')
    print('동굴 속에는 착한 용과 무서운 용이 있다.')
    print('랜덤하게 동굴을 선택해 용을 만나면 보물을 획득하고, 나쁜 용을 만나면 죽습니다.')
    
def chooseCave():
    cave=''
    while cave!= '1' and cave != '2':
        print('동굴을 선택(1 또는 2)')
        cave = input()
    return cave
def chkCave(selectNum):
    print('동굴에 도착했습니다')
    time.sleep(3)
    rndNum = random.randint(1, 2)
    
    if selectNum ==str(rndNum):
        print('착한용을 만났지만 보물을 얻지 못했어요. 보물을 얻을 확률은 3%에요')
    else:
        print('죽었습니다.')

playAgain='y'
while playAgain == 'y':
    gameStart()
    caveNumber = chooseCave()
    chkCave(caveNumber)
    print('계속 할까요?(y or n)')
    playAgain = input()



    