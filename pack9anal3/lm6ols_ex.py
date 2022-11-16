# 회귀분석 문제 3) 
# kaggle.com에서 carseats.csv 파일을 다운 받아 (https://github.com/pykwon 에도 있음) 
# Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pack9anal3.lm6ols_condition import residual
plt.rc('font', family='malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf

df=pd.read_csv("../testdata/Carseats.csv")
print(df.head(3))
print(df.info()) # 6,9,10 번째는 object라 떠나보낼게요
df = df.drop([df.columns[6], df.columns[9], df.columns[10]], axis=1)
print(df.head(2))
print(df.corr()) # 상관계수 확인

lm =smf.ols(formula = 'Sales ~ Income + Advertising + Price + Age', data=df).fit()
#타당한 변수만 임의적으로 선택
print('요약결과:\n ', lm.summary())
# 넣어보고 P>|t| 가 0.05 보다 크면 빼~
# CompPrice 독립변수로써 의미는 있지만 상관계수가 너무 작다. 그렇기때문에 뺴는게 낫지않을까 해요(정답은아님)

df_lm=df.iloc[:,[0,2,3,5,6]] #모든행의  [0,2,3,5,6]열
print(df_lm.head(3))

# 모델 저장
import joblib
joblib.dump(lm, 'yhs.model')
del lm
print('--지금부터는 저장된 모델을 읽어 사용함------')
lm= joblib.load('yhs.model')
# print(lm.summary())

print('--회귀 분석모형의 적절성 확인 작업')
# 잔차 구하기
fitted = lm.predict(df_lm)
residual = df_lm['Sales'] - fitted
print(residual[:3])
print('잔차의 평균 : ', np.mean(residual))
sns.regplot(fitted, residual, lowess=True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0,0], '--', color='blue')
plt.show()

print('정규성 ----')
import scipy.stats as stats
sr = stats.zscore(residual)
(x,y), _ = stats.probplot(sr)
sns.scatterplot(x,y)
plt.plot([-3,3], [-3,3], '--', color='blue')
plt.show()  # 잔차항이 정규뷴포를 따름

print('shapiro test : ', stats.shapiro(residual))

print('독립성 ----')
# Durbin-Watson: 1.931   2애 근사하므로 독립성 만족

print('등분산성 --- ')
sr= stats.zscore(residual)
sns.regplot(fitted, np.sqrt(abs(sr)), lowess=True, line_kws={'color':'red'})
plt.show() # 평균선을 기준으로 일정한 패턴을 보이지 않아 등분산성 만족

print('다중공선성 ---')
from statsmodels.stats.outliers_influence import variance_inflation_factor
df2 = df[['Income', 'Advertising', 'Price', 'Age']]
print(df2.head(2))
print(df2.shape) # (400, 4)
vifdf = pd.DataFrame()
vifdf['vif_value'] = [variance_inflation_factor(df2.values, i) for i in range(df2.shape[1])]
print(vifdf) # 모든 변수가 10을 넘기지 않음, 다중공산성 우려 없다.

# 모델 저장
import joblib
joblib.dump(lm, 'yhs.model')
del lm

print('--지금부터는 저장된 모델을 읽어 사용함------')
lm= joblib.load('yhs.model')
# print(lm.summary())


# 완성된 모델로 새로운 독립변수의 값을 주고 Sales를 예측
new_df = pd.DataFrame({'Income':[33,55,66], 'Advertising':[10,13,16],
                        'Price':[100,120,140], 'Age':[33,35,40]})
pred = lm.predict(new_df)
print('Sales에 대한 예측 결과 : \n', pred)
