# 어느 음식점 매출 자료와 날씨 자료를 활용하여 온도(추움, 보통, 더움)에 따른 매출액 평균의 차이를 검정해보자. - t-test 활용
# 데이터 두개 이상을 합쳐서 검정해보자. 요인은 온도 하나.
# 귀무 : 음식점 매출액의 평균은 온도에 영향이 없다.
# 대립 : 음식점 매출액의 평균은 온도에 영향이 있다.

import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

# 데이터는 data.go.kr을 참조
# 매출 자료 
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv", dtype={'YMD':'object'})
print(sales_data.head(3))
print(sales_data.info())  # 328 * 3 (328행 3열)
# 매출 자료 날짜 int로 되어있어 바꿔야 한다.

# 날씨 자료
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tweather.csv")
print(wt_data.head(3))
print(wt_data.info())

# 두 데이터를 병합: 날짜를 사용,  그래서 wt_data의 tm을 2018-06-01 ==> 20180601 형태로 변환

wt_data.tm = wt_data.tm.map(lambda x:x.replace('-','')) # 시리즈 데이터에서 한개 꺼내서 map 사용
print(wt_data.head(3))
print(wt_data.tail(3))

print('두 데이터 병합 - merge-')
frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm')  # left join
print(frame.head(5))
print(frame.tail(5))
print(len(frame))  # 328개 
# 공통칼럼을 가지고 두개의 데이터를 한개의 데이터로 만들 수 있다.
print()

# 분석에 사용할 열만 추출
print(frame.columns)  # ['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn', 'maxWs', 'avgWs', 'ddMes']
data = frame.iloc[:, [0, 1, 7, 8]]  # 'YMD', 'AMT', 'maxTa', 'sumRn'
print(data.head(3))

# 일별 최고온도(maxTa)를 구간설정을 해서 범주형 변수를 추가
print(data.maxTa.describe()) # mean 18, min -4.9, max 36.8

data['Ta_gubun'] = pd.cut(data.maxTa, bins=[-5, 8, 24, 37], labels=[0,1,2]) # 3구간(-5, 8 24, 24 37)
print(data.isnull().sum()) # 결측치 없음
print(data['Ta_gubun'].unique())

# 세 그룹의 매출액으로 정규성, 등분산성 확인
x1 = np.array(data[data.Ta_gubun == 0].AMT)
x2 = np.array(data[data.Ta_gubun == 1].AMT)
x3 = np.array(data[data.Ta_gubun == 2].AMT)
print(x1[:4])
print(x2[:4])
print(x3[:4])

# 정규성 검증
print(stats.ks_2samp(x1, x2).pvalue)  # 다 정규성 만족 못함 - 거의 0에 가까움
print(stats.ks_2samp(x1, x3).pvalue)
print(stats.ks_2samp(x2, x3).pvalue)

# 등분산성
print(stats.levene(x1, x2, x3).pvalue)  # 0.0390023 < 0.05 보다 작음 , 만족 못함
# bartlett() 사용못함

print('온도별 매출액 평균')
# pd.options.display.float_format = '{:.5f}'.format # 과학적 표기방법 해제?

spp = data.loc[:, ['AMT', 'Ta_gubun']]
print(spp.head(3))
print(spp.groupby('Ta_gubun').mean())

print(pd.pivot_table(spp, index=['Ta_gubun'], aggfunc='mean'))
#  1032362 vs 818106 vs 553710 차이가 있나???

# anova 진행
sp = np.array(spp)
print(sp[:3])
group1 = sp[sp[:, 1] == 0, 0]
group2 = sp[sp[:, 1] == 1, 0]
group3 = sp[sp[:, 1] == 2, 0]

# 데이터 분포 시각화 
# plt.boxplot([group1, group2 ,group3], showmeans = True)
# plt .show()

print()
print(stats.f_oneway(group1, group2 ,group3))
# F_onewayResult(statistic=99.1908012029983, pvalue=2.360737101089604e-34)
#=========================================================================================
# 해석 : p-value = 2.360737101089604e-34 < 0.05 이므로 귀무 기가. 음식점 매출액의 평균은 온도에 영향이 있다.
#=========================================================================================

# 정규성을  만족하지 않으므로 
print(stats.kruskal(group1, group2 ,group3))
# KruskalResult(statistic=132.7022591443371, pvalue=1.5278142583114522e-29)

# 등분산성을 만족하지 않으므로
# pip install pingouin
from pingouin import welch_anova
print(welch_anova(data=data, dv='AMT', between='Ta_gubun'))
#      Source  ddof1     ddof2           F         p-unc       np2
# 0  Ta_gubun      2  189.6514  122.221242  7.907874e-35  0.379038

# 각 지역의 평균 차이가 궁금. 사후 검정
# post hoc test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukeyResult = pairwise_tukeyhsd(endog=spp.AMT, groups=spp.Ta_gubun) # 알파값은 기본적으로 0.05다
print(tukeyResult)

# 시각화
tukeyResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()
