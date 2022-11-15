# mtcars dataset으로 단순/다중회귀 모델 작성 : ols() 사용
# 귀납적 추론: 개별적인 사실들로부터 일반적인 원리를 이끌어내는 추론방식이다. 
# 연역적 추론: 전제로부터 결론을 논리적으로 도출하는 추론방식이다.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars.head(3)) # [32 rows x 11 columns]
# print(mtcars.corr())
print(np.corrcoef(mtcars.hp, mtcars.mpg)[0,1]) # -0.7761683718265864
print(np.corrcoef(mtcars.wt, mtcars.mpg)[0,1]) # -0.8676593765172281

# 단순선형회귀 : mtcars.hp(feature, x), mtcars.mpg(label, y)
# 시각화
"""
plt.scatter(mtcars.hp, mtcars.mpg)
# 참고 : numpy의 polyfit()을 이용하면 slope, intercept를 얻을 수 있다.
slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, 1)
print('slope:{}, intercept:{}'.format(slope, intercept))
# slope:-0.06822, intercept:30.09886
plt.plot(mtcars.hp, slope * mtcars.hp + intercept)
plt.xlabel('마력수')
plt.ylabel('연비')
plt.show()
"""

result1 = smf.ols('mpg ~ hp', data=mtcars).fit() # 종속변수
print(result1.summary())
print()
print(result1.summary().tables[1])

print('마력수 110에 대한 연비는', -0.088895 * 110 + 30.0989) # 연비는 20.32045
print('마력수 50에 대한 연비는', -0.088895 * 50 + 30.0989)   # 연비는 25.65415
print('마력수 200에 대한 연비는', -0.088895 * 200 + 30.0989) # 연비는 12.3199

print('---------------')
# 다중선형회귀 : mtcars.hp, mtcars.wt(feature, x), mtcars.mpg(label, y)
result2 = smf.ols(formula='mpg ~ hp + wt', data=mtcars).fit() # 종속변수
print(result2.summary())
print(result2.summary().tables[1])
# 종속변수가 2개일때 - Adj. R-squared값 보기
print('마력수 110, 차체 무게 5톤에 대한 연비는', (-0.0318 * 110) + (-3.8778 * 5) + 37.2273)

print('predict 함수 사용')
# predict 함수 사용
new_data = pd.DataFrame({'hp':[110, 120, 150], 'wt':[5, 2, 7]})
new_pred = result2.predict(new_data)
print('예상 연비 : ', new_pred.values)

# 키보드 값 받기
new_hp =float(input('새로운 마력수 : '))
new_wt =float(input('새로운 차체 무게 : '))
new_data2 = pd.DataFrame({'hp':[new_hp], 'wt':[new_wt]})
new_pred2 = result2.predict(new_data2)
print('예상 연비 : ', new_pred2.values)
