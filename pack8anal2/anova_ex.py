import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import numpy as np
import urllib.request

# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

# 귀무 : 빵을 기름에 튀길 때 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다.
# 대립 : 빵을 기름에 튀길 때 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 있다.

data=pd.read_csv("../testdata/bbang.csv",delimiter=' ')
print(data.head(6))
print(data.shape)  # (20, 2)
print(data.isnull().sum())

data = data.fillna({'quantity':data['quantity'].mean()})
print(data)
print(data.isnull().sum())
print(data.describe())

result = data[['kind', 'quantity']]
k1 = result[result['kind']== 1]
k2 = result[result['kind']== 2]
k3 = result[result['kind']== 3]
k4 = result[result['kind']== 4]

quan1 = k1['quantity']
quan2 = k2['quantity']
quan3 = k3['quantity']
quan4 = k4['quantity']

print(quan1[:6])
print(quan2[:6])
print(quan3[:6])
print(quan4[:6])

print('평균 : ', np.mean(quan1), ' ', np.mean(quan2), ' ', np.mean(quan3), ' ', np.mean(quan4))

# 정규성 확인
# 한 개의 표본이 같은 분포를 따르는지 확인
print(stats.shapiro(quan1).pvalue)  # 0.86804  > 0.05 크므로 만족
print(stats.shapiro(quan2).pvalue)  # 0.59239
print(stats.shapiro(quan3).pvalue)  # 0.48601
print(stats.shapiro(quan4).pvalue)  # 0.41621

# 두 개의 표본이 같은 분포를 따르는지 확인
print(stats.ks_2samp(quan1, quan2).pvalue)  # 0.93073 > 0.05 크므로 만족
print(stats.ks_2samp(quan1, quan3).pvalue)
print(stats.ks_2samp(quan1, quan4).pvalue)
print(stats.ks_2samp(quan2, quan3).pvalue)
print(stats.ks_2samp(quan2, quan4).pvalue)
print(stats.ks_2samp(quan3, quan4).pvalue)

print()
# 등분산성 확인
print(stats.levene(quan1, quan2, quan3, quan4).pvalue)  # 0.32689 > 0.05 크므로 만족

# anova 진행
import statsmodels.api as sm
reg = ols('quantity ~ C(kind)', data=data).fit()
table =sm.stats.anova_lm(reg, type=2)
print(table)
#             df       sum_sq     mean_sq         F    PR(>F)
# C(kind)    3.0   231.304247   77.101416  0.266935  0.848244
# Residual  16.0  4621.432595  288.839537       NaN       NaN

#=========================================================
# 해석 : p-value = 0.848244 > 0.05 크므로 귀무채택.            =
# 빵을 기름에 튀길 때 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다.  =
#=========================================================

# 사후검증
# post hoc test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukeyResult = pairwise_tukeyhsd(endog= data.quantity, groups=data.kind) # 알파값은 기본적으로 0.05다
print(tukeyResult)   #          endog가 종속변수, groups가 독립변수



# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.

# 귀무 : 각 부서직원 연봉의 평균에 차이가 없다.
# 대립 : 각 부서직원 연봉의 평균에 차이가 있다.


import MySQLdb
import pickle
import sys

try : 
    with open('mydb.data', mode='rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('connect err : ', e)
    sys.exit()

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no, buser_name, jikwon_pay
        from jikwon, buser
        where jikwon.buser_num=buser.buser_no
        """
    cursor.execute(sql)
    # datas = pd.DataFrame.from_records(cursor.fetchall(), columns=['사번', '부서명', '연봉'])
    datas = pd.read_sql(sql, conn)
    
    df = pd.DataFrame(datas) # 중복 위에꺼ㅏ랑
    df.columns = '사번', '부서명', '연봉'
    df.index = range(1, 31)
    print("부서별 연봉의 평균 : ", df.groupby(['부서명'])['연봉'].mean())
    
    a = df[df['부서명'] == '관리부']
    b = df[df['부서명'] == '영업부']
    c = df[df['부서명'] == '전산부']
    d = df[df['부서명'] == '총무부']
    a_pay = a.loc[:,'연봉']
    b_pay = b.loc[:,'연봉']
    c_pay = c.loc[:,'연봉']
    d_pay = d.loc[:,'연봉']
    print('관리부 연봉',a_pay)
    print('영업부 연봉',b_pay)
    print('전산부 연봉',c_pay)
    print('총무부 연봉',d_pay)
    
    # 정규성 검증
    
    print(stats.shapiro(a_pay).pvalue)  # 0.90780 > 0.05  만족
    print(stats.shapiro(b_pay).pvalue)  # 0.02560 < 0.05  불만족
    print(stats.shapiro(c_pay).pvalue)  # 0.41940 > 0.05  만족
    print(stats.shapiro(d_pay).pvalue)  # 0.02604 < 0.05  불만족
     
    print()
    print(stats.ks_2samp(a_pay, b_pay).pvalue)  # 0.64065 > 0.05 / 다 정규성 만족함 
    print(stats.ks_2samp(a_pay, c_pay).pvalue)  
    print(stats.ks_2samp(a_pay, d_pay).pvalue)  
    print(stats.ks_2samp(b_pay, c_pay).pvalue)  
    print(stats.ks_2samp(b_pay, d_pay).pvalue)  
    print(stats.ks_2samp(c_pay, d_pay).pvalue)  

    # 등분산성
    print(stats.levene(a_pay, b_pay, c_pay, d_pay).pvalue) # 0.79807 > 0.05 만족
    
    print()
    print(stats.f_oneway(a_pay, b_pay , c_pay, d_pay))
    # F_onewayResult(statistic=0.41244077160708414, pvalue=0.7454421884076983)
    
    #===========================================================================
    # 해석 : p-value = 0.74544218 > 0.05 크므로 귀무가설 채택. 각 부서직원 연봉의 평균에 차이가 없다.
    #===========================================================================
    
    # 평균 차이가 궁금. 사후 검정
    # post hoc test
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    tukeyResult = pairwise_tukeyhsd(endog=datas.연봉, groups=datas.부서명) # 알파값은 기본적으로 0.05다
    print(tukeyResult)

except Exception as e:
    print("err : ", str(e))
finally:
    cursor.close()
    conn.close()




