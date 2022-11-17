# LinearRegression 으로 선형회귀분석모델을 작성 - mtcars dataset을 사용
import statsmodels.api
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error


mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars.head(3))
print(mtcars.corr(method='pearson'))

# hp가 mpg에 영향을 준다 라는 가정하에 모델을 생성
x= mtcars[['hp']].values # 반환값이 matrix type
print(x[:5])
y = mtcars['mpg'].values # 반환값이 vector type, vector 가로 한개만
print(y[:5])

# plt.scatter(x,y)
# plt.show()

lmodel = LinearRegression().fit(x,y)
print('회귀계수(slope) : ', lmodel.coef_)  # [-0.06822828]
print('회귀계수(intercept) : ', lmodel.intercept_)  # 30.098860539622496
print()
pred = lmodel.predict(x)
print('예측값 : ', np.round(pred[:5], 1))
print('실제값 : ', y[:5])

# 모델 성능 확인
print('MSE : ', mean_squared_error(y, pred))
print('R2(설명력) : ', r2_score(y, pred))

# 새로운 hp데이터로 예측
new_hp = [[110]] # matrix로 만들기
new_pred = lmodel.predict(new_hp)
print('%s 마력인 경우 연비는 %s입니다'%(new_hp[0][0], new_pred[0]))





