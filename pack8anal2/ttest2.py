# 두 집단의 가설검정 - 실습 시 분산을 알지 못하는 것으로 한정하겠다.
# * 서로 독립인 두 집단의 평균 차이 검정(independent samples t-test)
# 남녀의 성적 A 반과 B 반의 키 경기도와 충청도의 소득 따위의 서로 독립인 두 집단에서 얻은 표본을 독립표본 (two sample) 이라고 한다

from scipy import stats
import pandas as pd
from numpy import average

# 실습)
# 남녀 두 집단 간 파이썬 시험의 평균 차이 검정
male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]

# 귀무 : 남녀 두 집단 간 파이썬 시험의 평균 차이가 없다.
# 대립 : 남녀 두 집단 간 파이썬 시험의 평균 차이가 있다.

print(average(male), ' ', average(female))  # 83.8   72.24
print(83.8-72.24) # 차이 11.560

two_sample = stats.ttest_ind(male, female)  # 두 개의 표본에 대한 t-test 실시
print(two_sample)
# Ttest_indResult(statistic=1.233193127514512, pvalue=0.2525076844853278)
# 검증 통계량         
#===================================================================================
# 해석 : pvalue=0.2525076 > 0.05보다 크므로 귀무가설 채택. 남녀 두 집단 간 파이썬 시험의 평균 차이가 없다.
#===================================================================================

print('----------------------')
# 실습) 두 가지 교육방법에 따른 평균시험 점수에 대한 검정 수행 two_sample.csv
data = pd.read_csv("../testdata/two_sample.csv")
print(data.head(3), len(data))

# 귀무 : 두 가지 교육방법에 따른 평균시험 점수에 차이가 없다.
# 대립 : 두 가지 교육방법에 따른 평균시험 점수에 차이가 있다.

ms = data[['method', 'score']]
print(ms)
# 교육방법별로 데이터 분리
m1 =ms[ms['method']==1]
m2 =ms[ms['method']==2]

score1 = m1['score']
score2 = m2['score']
print(score1)
print(score2)
print(score1.isnull().sum())  # 0개
print(score2.isnull().sum())  # 2개  NaN - 평균값으로 대체(대부분 제거 하거나, 0 또는 평균으로 대체한다.)

sco1 = score1.fillna(score1.mean())
sco2 = score2.fillna(score2.mean())  # 평균으로 대체
print(sco2.isnull().sum())

# 정규성 검정
import matplotlib.pyplot as plt
import seaborn as sns
# sns.histplot(sco1, kde=True, color='r')
# sns.histplot(sco2, kde=True, color='y')
# plt.show()

print(stats.shapiro(sco1).pvalue) # 0.367990374565 > 0.05 정규성 만족
print(stats.shapiro(sco2).pvalue) # 0.671418964862 > 0.05 정규성 만족

# 등분산성
print(stats.levene(sco1, sco2).pvalue)   # 0.4568427112977609 > 0.05 등분산성 만족
print(stats.fligner(sco1, sco2).pvalue)  # 0.44323735267062647
print(stats.bartlett(sco1, sco2).pvalue) # 0.26789717886602216

result = stats.ttest_ind(sco1, sco2)  # 정규성 만족, 등분산성 만족
print('t-value:%.5f, p-value:%.5f'%result)  # t-value:-0.19649, p-value:0.84505
#===================================================================================
# 해석 : p-value:0.84505 > 0.05 보다 크므로 귀무 채택. 두 가지 교육방법에 따른 평균시험 점수에 차이가 없다.
#===================================================================================

print('------- 참고 ---------')
result = stats.ttest_ind(sco1, sco2, equal_var=True) # 이게 기본값 / 정규성 만족, 등분산성 만족
print('t-value:%.5f, p-value:%.5f'%result)
result = stats.ttest_ind(sco1, sco2, equal_var=False) # 정규성 만족, 등분산성 불만족
print('t-value:%.5f, p-value:%.5f'%result)

# result2 = stats.wilcoxon(sco1, sco2)   # 정규성을 만족하지 않은 경우 -err 발생
# print('t-value:%.5f, p-value:%.5f'%result2)  -  err 발생
result2 = stats.mannwhitneyu(sco1, sco2) # 정규성을 만족하지 않은 경우
print('t-value:%.5f, p-value:%.5f'%result2)



