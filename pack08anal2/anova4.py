# Two-way ANOVA(이원분산분석) : 요인이 복수 - 각 요인의 그룹도 복수
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import statsmodels.api as sm

plt.rc('font', family='malgun gothic')

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3_2.txt"
data = pd.read_csv(urllib.request.urlopen(url), delimiter=',')
print(data.head(3), data.shape) # (36, 3)
print()

# data.boxplot(column='머리둘레', by='태아수', grid=False)
# plt.show()
# data.boxplot(column='머리둘레', by='관측자수', grid=False)
# plt.show()

# 귀무 : 태아수와 관측자수는 태아의 머리둘레와 관연이 없다.
# 대립 : 태아수와 관측자수는 태아의 머리둘레와 관연이 있다.

# 상호 작용을 빼고 한 경우
reg = ols("data['머리둘레'] ~ C(data['태아수']) + C(data['관측자수'])", data=data).fit()
result = anova_lm(reg, type=2)
print(result)

print()
# 상호 작용(교호작용, interaction이란 한 요인의 효과가 자른 요인의 수준에 의존하는 경우를 말한다.)을 한 경우
reg2 = ols("머리둘레 ~ C(태아수) + C(관측자수) + C(태아수):C(관측자수)", data=data).fit()  # C(태아수):C(관측자수) -> 상호작용
result2 = anova_lm(reg2, type=2)
print(result2) # C(태아수):C(관측자수) -> 이 값을 가지고 p-value 체크하기
#==================================================================================
# 해석 : p-value 0.3295509 > 0.05 이므로 귀무가설 채택. 태아수와 관측자수는 태아의 머리둘레와 관연이 없다.
#==================================================================================






