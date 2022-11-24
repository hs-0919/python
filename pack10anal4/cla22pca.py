# 특성공학 기범 중 차원 축소(PCA - 주성분 분석 / 비지도 학습)
# n개의 관측치와 p개의 변수로 구성된 데이터를 상관관계가 최소화된 k개의 변수로 축소된 데이터를 만든다.
# 데이터의 분산을 최대한 보존하는 새로운 축을 찾고 그 축에 데이터를 사용시키는 기법. 직교
# 목적 : 독립변수(x, feature)의 갯수를 줄임. 이미지 차원 축소로 용량을 최소화

# iris dataset으로 PCA를 진행
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
n =10
x = iris.data[:n, :2]
print(x, x.shape, type(x))
print(x.T)

# plt.plot(x.T, 'o:') # 'o' -모양이 동그라미
# plt.xticks(range(2))
# plt.grid()
# plt.legend(['표본{}'.format(i) for i in range(n)])
# plt.show()

"""
# 산점도
df = pd.DataFrame(x)
# print(df)
ax = sns.scatterplot(0, 1, data=pd.DataFrame(x), marker='s', s=100, color=['b']) # marker='s' 모양 square
for i in range(n):
    ax.text(x[i,0] - 0.05, x[i, 1] - 0.07, '표본{}'.format(i+1))
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 너비')
plt.axis('equal') # 너비 높이 같아지게?
plt.show()
"""
print()
# PCA
pca1 = PCA(n_components=1) # n_components 변환할 차원수 입력
x_low = pca1.fit_transform(x) # 근사값 찾는거 , 비지도 학습(타겟이 없다.), 차원축소된 근사 데이터
print('x_low : ', x_low, ' ', x_low.shape) # (10, 1)

x2 = pca1.inverse_transform(x_low)  # 차원 축소된 근사 데이터를 리버스, 회복
print('원복된 결과 : ', x2, ' ', x2.shape)
print(x)
print(x_low[0]) # [0.30270263]
print(x2[0, :]) # [5.06676112 3.53108532]
print(x[0])     # [5.1 3.5]

"""
# 시각화
ax = sns.scatterplot(0, 1, data=pd.DataFrame(x), marker='s', s=100, color='0.3') # marker='s' 모양 square
for i in range(n):
    d = 0.03 if x[i, 1] > x2[i,1] else -0.04
    ax.text(x[i,0] - 0.05, x[i, 1] - d, '표본{}'.format(i+1))
    plt.plot([x[i,0], x2[i,0]], [x[i,1], x2[i,1]], 'k-')
    
    
plt.plot(x2[:, 0], x2[:, 1], 'o-', color='b', markersize=10)
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 너비')
plt.axis('equal') # 너비 높이 같아지게?
plt.show()
"""

# iris 4개의 열을 모두 참여 -> 2개 열로 축소
x= iris.data
pca2 =PCA(n_components = 2)
x_low2 = pca2.fit_transform(x)
print('x_low2 : ', x_low2[:3], ' ', x_low2.shape)
print(pca2.explained_variance_ratio_) # 변동성 비율 / 전제 변동성에서 개별 PCA 결과(개별 component) 별로 차지하는 변동성 비율을 제공
# [0.92461872 0.05306648] - 0.92461872 주성분1이 92%, 0.05306648 주성분2가 5% => 합치면 97%설명력을 가짐(오차가 많이 없다)

x4 = pca2.inverse_transform(x_low2)
print('최초 자료 : ', x[0])
print('차원 축소 : ', x_low2[0])
print('차원 복귀 : ', x4[0]) # PCA를 통해 근사행렬로 변환됨

print()
iris2 = pd.DataFrame(x_low2, columns=['f1', 'f2'])
print(iris2.head(3)) # 이거 가지고 작업을 하면 된다. / 새로운 데이터도 주성분 분석하고 그걸가지고 작업해라

