
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api

# 회귀분석 문제 2) 
# testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
# 이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오. 수학점수를 종속변수로 하자.
# - 국어 점수를 입력하면 수학 점수 예측
# - 국어, 영어 점수를 입력하면 수학 점수 예측


stu = pd.read_csv("../testdata/student.csv")
print(stu.head(3))
print(stu.corr())


# 국어 점수를 입력하면 수학 점수 예측
result1 = smf.ols('수학 ~ 국어', data=stu).fit() # 종속~독립 (변하는값 수학)
print(result1.summary())

# 키보드 값 받기
new_han =float(input('국어 점수 : '))
new_data = pd.DataFrame({'국어':[new_han]})
new_pred = result1.predict(new_data)
print('예상 수학 점수 : ', new_pred.values)


# 국어, 영어 점수를 입력하면 수학 점수 예측

result2 = smf.ols(formula='수학 ~ 국어+영어', data=stu).fit()
print(result2.summary())

# 키보드 값 받기
new_han =float(input('국어 점수 : '))
new_eng =float(input('영어 점수 : '))
new_data2 = pd.DataFrame({'국어':[new_han], '영어':[new_eng]})
new_pred2= result2.predict(new_data2)
print('예상 수학 점수 : ', new_pred2.values)

'''
# 회귀분석 문제 2) 
# testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
# 이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.  수학점수를 종속변수로 하자.
#   - 국어 점수를 입력하면 수학 점수 예측
#   - 국어, 영어 점수를 입력하면 수학 점수 예측

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf


student = pd.read_csv("../testdata/student.csv")
print(student.head(3))

print(' --- 국어 점수를 입력하면 수학 점수 예측 --- ')
jums = smf.ols('수학 ~ 국어', data=student).fit()
print(jums.summary())
print(jums.conf_int(alpha=0.05))
print()
print(jums.summary().tables[1])

print('국어점수 90점을 받은 학생 수학 점수 예측. . . 두둥 ', 0.5705*90+32.1069)
print('국어점수 70점을 받은 학생 수학 점수 예측. . . 두둥 ', 0.5705*90+32.1069)


result = smf.ols(formula='수학 ~ 국어 + 영어', data=student).fit()
print(result.summary())
print(result.summary().tables[1])

print(' --- 국어, 영어 점수를 입력하면 수학 점수 예측 --- ')
korjum = float(input('국어점수 : '))
engjum = float(input('영어점수 : '))
print('국어점수 {}, 영어점수 {}로 예측한 수학점수는 '.format(korjum, engjum), 0.1158*korjum + 0.5942 *engjum + 22.6238 )

print('predict 함수 사용')
new_data = pd.DataFrame({'국어' : [80,90,85],'영어':[100,80,90]})
new_pred = result.predict(new_data)
print('예상 수학 점수 : ',new_pred.values)
'''
