import pandas as pd
import scipy.stats as stats

# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
#   조건 :  level, pass에 대해 NA가 있는 행은 제외한다.

data1 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/cleanDescriptive.csv").dropna(subset=['level', 'pass'])
print(data1.head(4))
# print(data1.describe)
print(data1.isnull().sum()) # 이원 카이저 검정에는 크로스테이블이 필요하다

print(data1['level'].unique())  # [1. 2. 3.]  고졸, 대졸, 대학원졸
print(data1['pass'].unique())  # [2. 1.]    1 - 합격, 2 - 불합격


# 귀무 가설 : 부모학력 수준이 자녀의 진학여부와 관련이 없다.
# 대립 가설 : 부모학력 수준이 자녀의 진학여부와 관련이 있다.

ctab = pd.crosstab(index=data1['level'], columns=data1['pass']) # 독립 변수 - 부모학력 수준
ctab.columns = ['합격', '불합격']
ctab.index=['고졸', '대졸', '대학원졸']
print(ctab)

chi2, p, ddof, _ = stats.chi2_contingency(ctab)
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, ddof))
# chi2:2.7669, p:0.25070, ddof:2
#===============================================================================
# 해석 : p:0.25070 > 0.05 보다 크므로 귀무가설 채택. - 부모학력 수준이 자녀의 진학여부와 관련이 없다.
#===============================================================================

print('-----------------------------')
# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
# 그렇다면 jikwon_jik과 jikwon_pay 간의 관련성 여부를 통계적으로 가설검정하시오.
#   예제파일 : MariaDB의 jikwon table 
#   jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#   조건 : NA가 있는 행은 제외한다.

# 귀무 :직급과 연봉은 관련이 없다.
# 대립 :직급과 연봉은 관련이 있다.

import MySQLdb
import pickle

with open('mydb.data', mode='rb') as obj:
    config = pickle.load(obj) # 이렇게만 쓰는것은 아니다.

try:
    conn= MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = "select jikwon_jik, jikwon_pay from jikwon"
    cursor.execute(sql)
    
    ar=[]
    for data in cursor.fetchall():
        jik = 0
        pay = 0
        if data[0] == '이사':
            jik = 1
        elif data[0] == '부장':
            jik = 2
        elif data[0] == '과장':
            jik = 3
        elif data[0] == '대리':
            jik = 4
        elif data[0] == '사원':
            jik = 5
        else:
            jik = 0
        
        if 1000 <= data[1] < 3000:
            pay = 1
        elif 3000 <= data[1] < 5000:
            pay = 2
        elif 5000 <= data[1] < 7000:
            pay = 3
        elif 7000 <= data[1]:
            pay = 4
        else:
            pay = 0
            
        ar.append((jik, pay))
        
    # print(ar)
    df = pd.DataFrame(ar, columns= ['직급', '연봉']).dropna()
    print(df.head(3))
    ctab2 = pd.crosstab(index=df['직급'], columns = df['연봉'])
    ctab2.index = ['이사', '부장', '과장', '대리','사원']
    ctab2.columns = ['1,2천', '3,4천', '5,6천','7천이상']
    print(ctab2)
    
    chi2, p, ddof, _ = stats.chi2_contingency(ctab2)
    print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, ddof))
    
except Exception as e:
    print('err : ', e)
finally:
    cursor.close()
    conn.close()

# chi2:37.403493, p:0.0001921, ddof:12
#===============================================================================
# 해석 : p:0.0001921 < 0.05보다 작으므로 귀무가설 기각. 직급과 연봉은 관련이 있다.
#===============================================================================

