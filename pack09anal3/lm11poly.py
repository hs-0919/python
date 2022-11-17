# 선형회귀모델을 다항회귀모델로 변환
# 선형 가정이 신뢰도가 떨어질 경우 대처방법으로 다항식을 추가할 수 있다.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([4,2,1,3,7])

print(np.corrcoef(x,y))

# plt.scatter(x,y)
# plt.show()

# 선형회귀모델 작성
from sklearn.linear_model import LinearRegression

x=x[:, np.newaxis]  # 차원 확대 - sklearn을 쓰기 때문에 차원확대~
# print(x)
model = LinearRegression().fit(x,y)
y_pred = model.predict(x)
print(y_pred) # [2.  2.7 3.4 4.1 4.8]

# plt.scatter(x,y)
# plt.plot(x, y_pred, c='red')
# plt.show()

# 좀 더 복잡한 형태의 모델을 필요 : 다항식 특징(feature)을 추가한 다항회귀모델 작성
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=3, include_bias=False) # degree는 열의 객수 
x2 = poly.fit_transform(x) # 다항식이 추가됨, 특징행렬 작성
print(x2)

model2 = LinearRegression().fit(x2,y)  # 특징행렬 값으로 학습
y_pred2 = model2.predict(x2)
print(y_pred2)

plt.scatter(x,y)
plt.plot(x, y_pred2, c='red')
plt.show() # 비선형모델

