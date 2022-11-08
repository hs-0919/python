import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from numpy import average

# [two-sample t 검정 : 문제1] 
# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.

blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red =  [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]

# 귀무 : 동일한 상품의 포장지 색상에 따른 제품의 매출액 차이가 없다.
# 대립 : 동일한 상품의 포장지 색상에 따른 제품의 매출액 차이가 있다.

print(average(blue), ' ', average(red))   # 72.81  63.81  
print(72.81 - 63.81)   # 차이 : 9.0

# 정규성 검정
print(stats.shapiro(blue).pvalue)  # 0.5102 > 0.05
print(stats.shapiro(red).pvalue)

two_sample1 = stats.ttest_ind(blue, red)  # 두 개의 표본에 대한 t-test 실시
print(two_sample1) # statistic=2.9280203225212174, pvalue=0.008316545714784403
#===========================================================================================
# 해석 : pvalue=0.00831 < 0.05 보다 작으므로 귀무가설 기각. 동일한 상품의 포장지 색상에 따른 제품의 매출액 차이가 있다.
#===========================================================================================


# [two-sample t 검정 : 문제2]  
# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.

# 귀무 : 무작위 남녀에 대한 혈관 내의 콜레스테롤 양에 차이가 없다.
# 대립 : 무작위 남녀에 대한 혈관 내의 콜레스테롤 양에 차이가 있다.
import random

male =   [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
female = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]

random.seed(123)
male = random.sample(male, 15)
female = random.sample(female, 15)

print(average(male), ' ', average(female))  # 3.22 vs 3.27

# 정규성 검정
print(stats.shapiro(male).pvalue)    # 0.03762 < 0.05 정규성 만족 안함
print(stats.shapiro(female).pvalue)  # 0.00149 < 0.05 정규성 만족 안함

# two_sample2 = stats.ttest_ind(male, female) # 정규성 만족 못하므로 ttest_ind 사용 못함
print(stats.wilcoxon(male, female)) # wilcoxon 사용해야 한다.
# statistic=59.0, pvalue=0.97796630859375
#=====================================================================================
# 해석 : pvalue=0.97796 > 0.05 보다 크므로 귀무 채택. 무작위 남녀에 대한 혈관 내의 콜레스테롤 양에 차이가 없다.
#=====================================================================================


# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.

# 귀무 : 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하지 않는다.
# 대립 : 총무부, 영업부 직원의 연봉의 평균에 차이가 존재한다.

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
        select jikwon_no, buser_num, buser_name, jikwon_pay
        from jikwon, buser
        where jikwon.buser_num=buser.buser_no
        """
    cursor.execute(sql)
    datas=cursor.fetchall() # df = pd.read_sql(sql, conn)
    
    df = pd.DataFrame(datas)
    df.columns = '사번', '부서번호', '부서명', '연봉'
    df.index = range(1, 31)
    # print(df.head(2))
    # print("부서별 연봉의 합 : ", df.groupby(['부서명'])['연봉'].sum())
    print("부서별 연봉의 평균 : ", df.groupby(['부서명'])['연봉'].mean())
    
    a = df[df['부서명'] == '총무부']
    a_pay = a.loc[:,'연봉']
    # print(a_pay)
    b = df[df['부서명'] == '영업부']
    b_pay = b.loc[:,'연봉']
    # print(b_pay)
    
    # 정규성 검정
    print(stats.shapiro(a_pay).pvalue)  # 0.026044 < 0.05 정규성 만족 안함
    print(stats.shapiro(b_pay).pvalue)  # 0.025608 < 0.05 정규성 만족 안함
    
    print(stats.mannwhitneyu(a_pay, b_pay))
    # statistic=51.0, pvalue=0.47213346080125185
    
    # print(stats.wilcoxon(a_pay_mean, b_pay_mean))  err
    # err :  The samples x and y must have the same length. wilcoxon 사용 못함
    # print(stats.ttest_ind(a_pay_mean, b_pay_mean)) # 정규성 만족 못하므로 ttest_ind 사용 못함

except Exception as e:
    print("err : ", str(e))
finally:
    cursor.close()
    conn.close()

#=======================================================================================
# 해석 : pvalue=0.47213 > 0.05보다 크므로 귀무 채택. 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하지 않는다.
#=======================================================================================


# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 
# 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
test1 = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
test2 = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

# 귀무 : 학급의 학업능력이 변화했다고 말할 수 없다.
# 대립 : 학급의 학업능력이 변화했다고 말할 수 있다.

print(np.mean(test1), ' ', np.mean(test2))  # 중간: 74.16 / 기말: 81.66
print(stats.ttest_rel(test1, test2)) # statistic=-2.6281127723493993, pvalue=0.023486192540203194
#===============================================================================
# 해석 : pvalue=0.02348 < 0.05 이므로 귀무 기각. 이 학급의 학업능력이 변화했다고 말할 수 있다.
#===============================================================================

