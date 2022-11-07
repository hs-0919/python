# 이원카이제곱
# 동질성 검정 - 두 집단의 분포가 동일한가? 다른 분포인가? 를 검증하는 방법이다. 두 집단 이상에서 각 범주(집단) 간의 비율이 서로
# 동일한가를 검정하게 된다. 두 개 이상의 범주형 자료가 동일한 분포를 갖는 모집단에서 추출된 것인지 검정하는 방법이다.

import pandas as pd
import scipy.stats as stats

# 동질성 검정실습1) 교육방법에 따른 교육생들의 만족도 분석 - 동질성 검정 survey_method.csv
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/survey_method.csv")
print(data.head(3))
print(data.method.unique())  # [1 2 3]
print(data.survey.unique())  # [1 2 3 4 5]


# 귀무 : 교육방법에 따른 교육생들의 만족도에 차이가 없다.
# 대립 : 교육방법에 따른 교육생들의 만족도에 차이가 있다.

ctab = pd.crosstab(index=data.method, columns=data.survey)
ctab.columns = ['매우만족', '만족', '보통', '불만족', '매우 불만족']
ctab.index = ['방법1', '방법2', '방법3']
print(ctab)

chi2, p, ddof, _ = stats.chi2_contingency(ctab)  # 교차표의 결과를 직접 적용해도 됨.
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, ddof))
# chi2:6.5446, p:0.58645, ddof:8
#===============================================================================
# 해석 : p:0.58645 > 0.05보다 크므로 귀무가설 채택. 교육방법에 따른 교육생들의 만족도에 차이가 없다.
#===============================================================================

print('---------------------')

# 동질성 검정 실습2) 
# 연령대별 sns 이용률의 동질성 검정
# 20대에서 40대까지 연령대별로 서로 조금씩 그 특성이 다른 SNS 서비스들에 대해 이용 현황을 조사한 자료를 바탕으로 연령대별로 홍보
# 전략을 세우고자 한다.
# 연령대별로 이용 현황이 서로 동일한지 검정해 보도록 하자

# 귀무  :연령대별로 SNS 서비스 이용 현황은 서로 동일하다.
# 대립  :연령대별로 SNS 서비스 이용 현황은 서로 동일하지 않다.

data2= pd.read_csv("../testdata/snsbyage.csv")
print(data2.head(3), len(data2))
print(data2['age'].unique())      # [1(20대), 2(30대), 3(40대)]
print(data2['service'].unique())  # ['F' 'T' 'K' 'C' 'E']


ctab2 = pd.crosstab(index=data2.age, columns=data2.service)
print(ctab2)

chi2, p, ddof, _ = stats.chi2_contingency(ctab2) 
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, ddof))

# chi2:102.75202, p:1.1679064204212775e-18, ddof:8
#===============================================================================
# 해석 : p:1.1679064204212775e-18(0으로 봐야함) < 0.05 작으므로 귀무 기각. 
#      1439명 대상으로 연령대별로 SNS 서비스 이용 현황을 검증해본 결과 서로 동일하지 않다.
#===============================================================================






