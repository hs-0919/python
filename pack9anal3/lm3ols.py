# 단순선형회귀 모델
# 기본적인 결정론적 선형회귀 방법 : 독립변수에 대해 대응하는 종속변수와 유사한 예측값을 출력하는 함수 f(x)를 찾는 작업이다.
import pandas as pd

df = pd.read_csv("../testdata/drinking_water.csv")
print(df.head(3))
print(df.corr())

import statsmodels.formula.api as smf

# 적절성이 만족도에 영향을 준다라는 가정하에 모델 생성
model =smf.ols(formula = '만족도 ~ 적절성', data=df).fit()
print(model.summary()) # 생성된 모델의 요약결과를 반환. 능력치를 확인.

# Prob (F-statistic):2.24e-52 이게 p-value 값
# coef(0.7393)/std err(0.038) = t(19.340)
# F-statistic: 374.0 -> t값을 거듭제곱(**)하면 나옴
# 표본 평균들의 표준편차 : std err(표준오차, 작을 수록 좋다)

# 데이터의 밀도가 높으면 -> 표준오차가 작고, 분산의 설명력이 커진다(R-squared-결정계수(설명력)).
# R-squared(결정계수) - x가 종속변수 y의 분산을 설명하는 비율 (0.588-58.8%), 단순회귀설명 / 다중회귀설명은 Adj. R-squared

# 데이터의 밀도가 작으면(퍼지면) -> 표준오차가 크고, 분산의 설명력이 작아짐 / f값과 p값은 반비례
# p값이 0.05보다 크면 표는 볼것도 없다 - 유의하지 않다.

# t = 기울기/표준오차 = 평균1-평균2/표준오차

# Jarque-Bera (JB), Prob(JB) : 적합도 검정
# Kurtosis : 첨도

# ols 사용하기! 텐서플로 하고나서

print()
print('회귀계수 : ', model.params) # 회귀계수 : Intercept 0.778858
print('결정계수 : ', model.rsquared) # 결정계수 :  0.5880630629464404
print('유의확률 값 : ', model.pvalues) # 유의확률 값 : Intercept 1.454388e-09
print('예측값 : ', model.predict()[:5]) # 예측값 :  [3.73596305 2.99668687 3.73596305 2.25741069 2.25741069]
print('실제값 : ', df.만족도[:5].values) # 실제값 :  [3 2 4 2 2]

print()
new_df = pd.DataFrame({'적절성':[4,3,2,1]})
new_pred = model.predict(new_df)
print('예측 결과 : ', new_pred)
# 예측 결과 : 
# 0    3.735963
# 1    2.996687
# 2    2.257411
# 3    1.518135

