# 선형회귀분석모델 작성시 LinearRegression을 사용 - summary() 함수를 지원x
# 선형회귀분석모델을 평가할 수 있는 score 알아보기
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler # 정규화 지원
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error 
# mean_squared_error(평균제곱근오차)- 이거 꼭 알아놔라 딥러닝 텐서플로에 나온다
from sklearn.linear_model import LinearRegression
# sklearn에서 LinearRegression에 matrix로 만들어서 넣어야 한다.
# sklearn 은 feature는 무조건 matrix(2차원),  label은 vector나 matrix
import matplotlib.pyplot as plt


# 편차가 있는 표본 데이터를 작성
sample_size = 100 
np.random.seed(1)

print('표준편차가 같은 두 개의 변수를 생성 : 분산이 작음')
x = np.random.normal(0, 10, sample_size)
y = np.random.normal(0, 10, sample_size) + x * 30
print(x[:5])
print(y[:5])
print('상관계수: ', np.corrcoef(x, y)) # 0.99939357(현실세계에선 볼 수 없는 값)

# 독립변수 x에 대한 정규화 진행
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1, 1))
print(x_scaled[:5]) # 

# 시각화
# plt.scatter(x_scaled, y)
# plt.show()

model = LinearRegression().fit(x_scaled, y)
y_pred = model.predict(x_scaled)
print('예측값 : ', y_pred[:5])
print('실제값 : ', y[:5])
# print(model.summary()) AttributeError: 'LinearRegression' object has no attribute 'summary'
print()
# 모델 성능 파악용 함수 작성
def RegScore_func(y_true, y_pred):
    print('r2_score(결정계수, 설명력) :{}'.format(r2_score(y_true, y_pred)))
    print('explained_variance_score(설명분산점수) :{}'.format(explained_variance_score(y_true, y_pred)))
    print('mean_squared_error(MSE, 평균제곱오차) :{}'.format(mean_squared_error(y_true, y_pred)))
    # RMSE : 평균오차제곱근
    # 평균제곱오차 : 예측값에서 실제값(관찰값)을 뺀 값의 제곱의 합을 표본수로 나눈 것 
RegScore_func(y, y_pred) # (실제값, 예측값)

print()
print('표준편차가 같은 두 개의 변수를 생성 : 분산이 큼')
x = np.random.normal(0, 1, sample_size)
y = np.random.normal(0, 500, sample_size) + x * 30
print(x[:5])
print(y[:5])
print('상관계수: ', np.corrcoef(x, y)) # 0.00401167

# 독립변수 x에 대한 정규화 진행
scaler2 = MinMaxScaler()
x_scaled2 = scaler.fit_transform(x.reshape(-1, 1))
print(x_scaled2[:5]) #

# 시각화
plt.scatter(x_scaled2, y)
plt.show()

model2 = LinearRegression().fit(x_scaled2, y)
y_pred2 = model2.predict(x_scaled2)
print('예측값 : ', y_pred2[:5])
print('실제값 : ', y[:5])
# print(model.summary()) AttributeError: 'LinearRegression' object has no attribute 'summary'

print()
# 모델 성능 파악용 함수 작성
def RegScore_func2(y_true2, y_pred2):
    print('r2_score(결정계수, 설명력) :{}'.format(r2_score(y_true2, y_pred2)))
    print('explained_variance_score(설명분산점수) :{}'.format(explained_variance_score(y_true2, y_pred2)))
    print('mean_squared_error(MSE, 평균제곱오차) :{}'.format(mean_squared_error(y_true2, y_pred2)))
    # RMSE : 평균오차제곱근
    # 평균제곱오차 : 예측값에서 실제값(관찰값)을 뺀 값의 제곱의 합을 표본수로 나눈 것 
RegScore_func(y, y_pred2) # (실제값, 예측값)
