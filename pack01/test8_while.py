# 반복문 while 
# while 조건 : ~ 참이면 수행 

a =1
while a <= 5:
    print(a, end=' ')
    a += 1
    
print('while 수행 후 %d'%a)

print()
i=1
while i<=3:
    j=1
    while j<4:
        print('i:'+str(i) + ', j:' +str(j))
        j =j+1
    i += 1

print('1~100 사이의 정수 중 3의 배수의 합 출력')
i=1; hap=0
while i<100:
    if i % 3 == 0:
        # print(i, end=' ')
        hap += i
    i += 1
    # print(i, end=' ')

print('합은 {}'.format(hap))

print()
colors=['r', 'g', 'b']
print(colors[0])
a=0
while a<len(colors):
    print(colors[a], end=' ')
    a +=1

print()

while colors:
    print(colors.pop(0), end=' ')
    # print(len(colors))
    
print()
i=1
while i <= 10:
    j=1
    re=''
    while j<=i:
        re =re + '*'
        j += 1
    print(re)
    i += 1

print('-------------')
import time
#time.sleep(3)
sw =input('폭탄 스위치를 누를까요?[y/n]')
if sw == 'Y' or sw == 'y':
    count =5
    while 1 <= count:
        print('%d 초 남았습니다.'%count)
        time.sleep(1)
        count -= 1
    print('폭발합니다.')
elif sw == 'N' or sw == 'n':
    print('작업 취소')
else:
    print('y 또는 n을 누르세요')
    
print('end')


# 문1) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
i=0; hap=0
while i<=100:
    i += 1
    if i % 3 == 0 and not i % 2 == 0: # i % 2 != 0
        print(i, end=' ')
        hap += i
    
print('합은 {}'.format(hap))

#문2) 2 ~ 5 까지의 구구단 출력
i=1
while i < 5:
    i += 1
    j = 1
    while j <10:
        print(i, 'X', j, '=', i*j)
        j += 1

#문3) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
i=1
cnt=1
tot=0

while i<100:
    if cnt % 2 ==0: # 짝수 위치 숫자 처리
        tot += i
        print(i, end =' ')
    else:  # 홀수 위치 숫자 처리
        k = i * -1 # 부호 변경
        tot += k
        print(k, end=' ')
    cnt += 1
    i += 2 # 증가치 2
print('\ntot : ', tot)


# 문4) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
aa=2
count=0

while aa<=1000:
    imsi =False
    bb=2;
    
    while bb<= aa -1:
        if aa % bb == 0:
            imsi = True
        bb += 1
        
    if imsi == False:
        print(aa, end=' ')
        count += 1
    aa += 1
print('\ncount : ', count)
    
