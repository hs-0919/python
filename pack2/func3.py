# 변수에 생존 범위, 생존 시간 (scope rule)
# 변수 접근 순서 : Local > Enclosing function > Global

player = '전국대표'   # 전역변수 

def funcSoccer():
    name='신기해'    # 지역변수
    print(name, player)
    
funcSoccer()
print(player)

print('-----------')
a=10; b=20; c=30; #전역변수
print('1) a:{}, b:{}, c:{}'.format(a,b,c)) # a=10; b=20; c=30;
def func1():
    a =40
    b =50
    c =100
    def func2():
        func2_local = 7
        global c # c는 전역변수로 바뀜 
        nonlocal b # b는 func1으로 올라감
        print('2) a:{}, b:{}, c:{}'.format(a,b,c)) # func1()- 기존값 a=40 ,b=50, c=30(global c로인하여 전역변수로 바뀜, 그래서 100이 아니라 30이다.) 
        c =60 # err : local variable 'c' referenced before assignment
              # global c-> c는 전역변수로 바뀌어서 기존 전역변수 c 값 30이 60바뀜.
        b =70 # nonlocal b -> b는 func1()의 b 값으로 되어서 기존 b의 값 50이 70으로 바뀜 
    func2()
    print('3) a:{}, b:{}, c:{}'.format(a,b,c)) # func1()- a=40, b=70, c=100
func1()
print('함수 수행 후) a:{}, b:{}, c:{}'.format(a,b,c)) # 글로벌 변수(전역변수)- a=10, b=20, c=60

