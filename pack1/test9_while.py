# 반복문 continue, break 

a=0
while a < 10:
    a += 1
    if a ==3:continue
    if a ==5:break
    print(a)
else: # while문이 정상적으로 수행되었는지 확인하기 위해 쓸 수 있다.
    print('while문 정상 수행')
print('while 수행 후 %d'%a)

print()
# 난수 발생 
import random
random.seed(2) # 랜덤한 값을 고정시키고 싶을때 사용, 
num = random.randint(1, 10)
#print(num)
# while True: #무한루프
#     print('1~`0 사이의 컴이 가진 예상 숫자 입력:')
#     guess = int(input())
#     if guess == num:
#         print('성공'*10)
#         break
#     elif guess < num:
#         print('더 큰 수 입력')
#     elif guess > num:
#         print('더 작은 수 입력')

# 의사 난수(pseudo random)
friend = ['tom', 'john', 'oscar']
print(friend)
print(random.choice(friend)) # 하나만 랜덤하게 선택
print(random.sample(friend, 2)) # 표본 랜덤하게 2개만 뽑기
random.shuffle(friend)
print(friend)





