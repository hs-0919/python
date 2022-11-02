
import MySQLdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic') # 한글깨짐 방지
plt.rcParams['axes.unicode_minus'] = False  # 음수 깨짐 방지 - 위 랑 세트로 다니면 좋다.
import pickle
import csv


try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)
    
except Exception as e:
    print('connect err : ', e)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = "select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_pay from jikwon inner join buser on buser_num=buser_no"
    cursor.execute(sql)
    
    # 사번, 이름, 부서명, 직급, 연봉을 읽어 DataFrame을 작성
    df1 = pd.DataFrame(cursor.fetchall(), 
                       columns=['jikwon_no', 'jikwon_name', 'buser_name', 'jikwon_jik','jikwon_pay'])
    print(df1)
    
    # DataFrame의 자료를 파일로 저장
    with open('직원저장.csv', mode='w', encoding='utf-8') as fo:
        writer = csv.writer(fo)
        for r in cursor:
            writer.writerow(r)
    
    # 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
    df = pd.read_sql(sql, conn)
    df.columns = ['번호','이름','부서','직급','연봉']
    print(df.groupby(['부서'])['연봉'].sum())
    print('연봉 최솟값 : ', df['연봉'].min())
    print('연봉 최댓값 : ', df['연봉'].max())
    
    # 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))
    
    ctab = pd.crosstab(df['부서'], df['직급'], margins=True)
    print(ctab)
    
    # 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    print('부서별 연봉 평균 : ', df.groupby(['부서'])['연봉'].mean())
    df3 = df.groupby(['부서'])['연봉'].mean()
    plt.barh(range(len(df3)), df3)
    plt.show()
    
except Exception as e:
    print('process err : ', e)


    # conn = MySQLdb.connect(**config)
    # cursor = conn.cursor()
    # sql = """
    #     select jikwon_name, gogek_no, gogek_name, gogek_tel
    #     from jikwon j, gogek g
    #     where j.jikwon_no = g.gogek_damsano;
    #     """
    # cursor.execute(sql)
    #
    # df2 = pd.read_sql(sql, conn)
    # df2.columns = ['직원이름','고객번호','고객이름','고객 전화번호']
    # # print(df2['직원이름'].fillna(df2['직원이름']))
    # print(df2)
    
    
# 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
try:
    
    sql1="""
        select j.jikwon_name, g.gogek_no, g.gogek_name, g.gogek_tel
        from jikwon j left outer join gogek g
        on j.jikwon_no=g.gogek_damsano
    """
    cursor.execute(sql1)
    
    df2=pd.DataFrame(cursor.fetchall(),
                     columns=['직원이름','고객번호','고객명','고객전화'])
    for i in df2.columns:
        df2['고객명']=df2['고객명'].fillna('담당 고객 X')
        df2[i]=df2[i].fillna(' ')
    print(df2)   
     
except Exception as e:
    print('process err : ', e)

finally:
    cursor.close()
    conn.close()






