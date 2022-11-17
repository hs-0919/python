# 일원분산분석으로 평균차이 검정 : 한 개의 요인에 따른 여러 개의 집단으로 데이터가 구성됨

# 강남구에 있는 GS편의점 3개 지역 알바생의 급여에 대한 평균차이 검정을 실시
# 귀무 : 강남구에 있는 GS편의점 알바생의 급여에 대한 평균은 차이가 없다.
# 대립 : 강남구에 있는 GS편의점 알바생의 급여에 대한 평균은 차이가 있다.

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import numpy as np
import urllib.request

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3.txt"
data = pd.read_csv(url, header=None)
# print(data.head())
# print(data.describe())
data = data.values
print(data[:3], type(data))

print()
data = np.genfromtxt(urllib.request.urlopen(url), delimiter=',') # matrix로 생성, class 'numpy.ndarray'
print(data[:3], type(data))

# 세 지역 급여 평균 확인
gr1 = data[data[:, 1]==1, 0]
gr2 = data[data[:, 1]==2, 0]
gr3 = data[data[:, 1]==3, 0]
print('gr1 : ', np.mean(gr1))  # 316.6
print('gr2 : ', np.mean(gr2))  # 256.4
print('gr3 : ', np.mean(gr3))  # 278.0  차이??

print()
# 정규성
print(stats.shapiro(gr1).pvalue)   # 0.333 > 0.05 정규성 만족
print(stats.shapiro(gr2).pvalue)
print(stats.shapiro(gr3).pvalue)

# 등분산성
print(stats.levene(gr1,gr2, gr3).pvalue) # 0.04584 < 0.05 만족 못함(만족했다고도 봐도 됨..)  웰치_아노바를 쓸 수 있따.
print(stats.bartlett(gr1,gr2, gr3).pvalue) 
# 표본수가 어느정도 있을때 - levene()
# 표본수가 적은경우 기준은 30개인데 기준은아니다 - bartlett()

# 데이터의 퍼짐 정도 시각화
# plt.boxplot([gr1,gr2, gr3], showmeans=True)
# plt.show()

# 일원분산분석 방법1 : anova_lm
df= pd.DataFrame(data, columns=['pay', 'group'])
print(df.head(3))

lmodel= ols('pay ~ C(group)', data=df).fit() # ols - 최소자승법(선형회귀에서 기울기구하는거) / 범주형 일때 C()를 두른다. / fit()- 학습하는거
print(anova_lm(lmodel, type=1))
#=============================================================================================
# 해석: p-value : 0.043589 < 0.05 이므로 귀무가설 기각. 강남구에 있는 GS편의점 알바생의 급여에 대한 평균은 차이가 있다.
#=============================================================================================

print()
# 일원분산분석 방법2 : f_oneway() / 이게더 편하다. f_twoway()는 없다
f_sta, pvalue = stats.f_oneway(gr1, gr2, gr3)
print('f통계량 : ', f_sta)    # f통계량 :  3.71133
print('유의확률 : ', pvalue)   # 유의확률 :  0.04358
 
 
# 각 지역의 평균 차이가 궁금. 사후 검정
# post hoc test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukeyResult = pairwise_tukeyhsd(endog=df.pay, groups=df.group) # 알파값은 기본적으로 0.05다
print(tukeyResult)

# 시각화
tukeyResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()



