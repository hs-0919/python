# while / if 연습문제
# 문1) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
i = hap = 0

while i <= 100:
    i += 1
    if i % 3 == 0 and i % 2 != 0:
        print(i, end = ' ')
        hap += i

print('합은 {}'.format(hap))


# 문2) 2 ~ 5 까지의 구구단 출력
print()
i = 2
while i < 6:
    j = 1
    while j < 10:
        print(i, '*' , j, '=', i * j, end = ' ')
        j += 1
    print()
    i += 1

# 문3) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
print()
i = 1
cnt = 1
tot = 0

while i < 100:
    if cnt % 2 == 0:  # 짝수 위치 숫자 처리
        tot += i
        print(i, end = ' ')
    else:   # 홀수 위치 숫자 처리
        k = i * -1  # 부호 변경
        tot += k
        print(k, end = ' ')

    cnt += 1
    i += 2   # 증가치 2

print('\ntot : ', tot)


# 문4) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
print()
aa = 2
count = 0

while aa <= 1000:
    imsi = False
    bb = 2;

    while bb <= aa - 1:
        if aa % bb == 0:
            imsi = True
        bb += 1

    if imsi == False:
        print(aa, end = ' ')
        count += 1
    aa += 1

print('\ncount : ', count)
