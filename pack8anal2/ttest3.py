# 어느 음식점 매출 자료와 날씨 자료를 활용하여 강수 여부에 따른 매출액 평균의 차이를 검정해보자. - t-test 활용
# 데이터 두개 이상을 합쳐서 검정해보자.
# 귀무 : 강수 여부에 따른 음식점 매출액의 평균에 차이가 없다.
# 대립 : 강수 여부에 따른 음식점 매출액의 평균에 차이가 있다.

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

print('두 집단 간의 매출액 평균 검정 : t-test 검증')
print(data.isnull().sum())  # 결측치 없음
# print(data['sumRn'] > 0)

# data['rain_yn']= (data['sumRn'] > 0).astype(int)  # 비가 오면 1이됨, 안오면 0
data['rain_yn']= (data.loc[:, ('sumRn')] > 0) * 1
print(data.head(3))

# boxplot으로 강수 여부에 따른 매출액 시각화
sp = np.array(data.iloc[:, [1,4]]) #1열과 4열 출력
# print(sp)
tgroup1 = sp[sp[:, 1] == 0, 0]  # 집단1 : 비안오는 그룹의 매출액
tgroup2 = sp[sp[:, 1] == 1, 0]  # 집단2 : 비오는 그룹의 매출액
# plt.plot(tgroup1)
# plt.show()
# plt.plot(tgroup2)
# plt.show()
plt.boxplot([tgroup1, tgroup2], meanline=True, showmeans=True, notch=True)
plt.show()

print('평균은 ', np.mean(tgroup1), ' ', np.mean(tgroup2))  # 761040.254 vs 757331.521  차이?

# 정규성 확인
print(stats.shapiro(tgroup1).pvalue)  #  0.056049  만족
print(stats.shapiro(tgroup2).pvalue)  #  0.882739

# 등분산성 확인
print(stats.levene(tgroup1, tgroup2).pvalue) #0.712345 만족
print(stats.ttest_ind(tgroup1, tgroup2, equal_var=True))
# statistic=0.10109828602924716, pvalue=0.919534587722196 - 반비례 관계
#  pvalue=0.91953 > 0.05 이므로 귀무 가설 채택 - 강수 여부에 따른 음식점 매출액의 평균에 차이가 없다.

