# DecisionTreeRegressor,RandomForestRegressor로 정량적인 예측 모델 생성 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score



boston = load_boston()
# print(boston.keys())
df_x=pd.DataFrame(boston.data, columns =boston.feature_names)
df_y=pd.DataFrame(boston.target, columns=['MEDV'])
df = pd.concat([df_x, df_y], axis=1) # 데이터결합, 행기준
print(df.head(3))
print(df.corr())

# 시각화 
cols = ['MEDV', 'RM', 'LSTAT']
# sns.pairplot(df[cols])
# plt.show()

# 단순 선형회귀모델
x = df[['LSTAT']].values
y = df['MEDV'].values
print(x[:3])
print(y[:3])

print('---------- DecisionTreeRegressor ----------')
model = DecisionTreeRegressor(criterion='mse', random_state=123).fit(x,y)  # mse = 평균제곱오차
print('예측값 : ', model.predict(x)[:5])
print('실제값 : ', y[:5])
print('결정계수 : ', r2_score(y, model.predict(x)))  # 95%의 설명력


print('---------- RandomForestRegressor ----------')
model2 = RandomForestRegressor(criterion='mse', n_estimators=100, random_state=123).fit(x,y)  # mse = 평균제곱오차
print('예측값 : ', model2.predict(x)[:5])
print('실제값 : ', y[:5])
print('결정계수 : ', r2_score(y, model2.predict(x)))  # 90%의 설명력


