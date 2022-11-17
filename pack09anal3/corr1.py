# 공분산 / 상관관계

import numpy as np
import matplotlib.pyplot as plt

# 공분산 예
print(np.cov(np.arange(1, 6), np.arange(2, 7))) # 공분산 2.5 - 양의 관계
print(np.cov(np.arange(10, 60, 10), np.arange(20, 70, 10))) # 공분산 250 - 양의 관계
print(np.cov(np.arange(1, 6), (3,3,3,3,3)))  # 공분산 0 - 서로 관계가 없다.
print(np.cov(np.arange(1, 6), np.arange(6, 1, -1)))  # 공분산 -2.5 - 음의 관계

print()
x = [8,3,6,6,9,4,3,9,3,4]
print('x의 평균 : ',np.mean(x))
print('x의 분산 : ',np.var(x))

# y = [9,3,7,6,1,5,2,9,8,4]
y = [90,30,70,60,10,50,20,90,80,40]
print('y의 평균 : ',np.mean(y))
print('y의 분산 : ',np.var(y))

# plt.scatter(x, y)
# plt.show()

print('x,y 공분산 : ', np.cov(x,y)[0,1])       # x,y 공분산 :  2.0
print('x,y 상관계수 : ', np.corrcoef(x,y)[0,1]) # x,y 상관계수 :  0.2826752

from scipy import stats
print(stats.pearsonr(x, y))
print(stats.spearmanr(x, y))

# 주의 : 곱분산이나 상관계수는 선형 데이터인 경우에 활용
m = [-3,-2,-1,0,1,2,3]
n = [9,4,1,0,1,4,9]

plt.scatter(m, n)
plt.show()

print('m,n 공분산 : ', np.cov(m,n)[0,1]) # 0.0
print('m,n 상관계수 : ', np.corrcoef(m,n)[0,1]) # 0.0

