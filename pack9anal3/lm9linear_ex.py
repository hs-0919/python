import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn.preprocessing import MinMaxScaler # 정규화 지원
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.linear_model import LinearRegression

consumo = pd.read_csv("../testdata/Consumo_cerveja.csv")
consumo = consumo.dropna()

print(consumo.head(5))
print(consumo.info())

x= consumo[['Consumo de cerveja (litros)']].values
print(x[:5])
y = consumo[['Temperatura Media (C)']].values
print(y[:5])

# plt.scatter(x,y)
# plt.show()

lmodel = LinearRegression().fit(x,y)
print('회귀계수(slope) : ', lmodel.coef_)  
print('회귀계수(intercept) : ', lmodel.intercept_)









