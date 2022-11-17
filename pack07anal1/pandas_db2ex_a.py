import MySQLdb
import pandas as pd
import pickle
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import sys 

try : 
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('connect err : ', e)
    sys.exit()
    
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no, jikwon_name, buser_name, jikwon_pay, jikwon_jik from jikwon
        inner join buser 
        on buser.buser_no = jikwon.buser_num
        """
    cursor.execute(sql)  
   
    df = pd.read_sql(sql, conn)
    df.columns = '사번','이름', '부서명', '연봉', '직급'
    df.index = range(1, 31)
    print(df.head(2))
    print()
    print("부서별 연봉의 합 : ", df.groupby(['부서명'])['연봉'].sum())
    print("부서별 연봉의 최대 : ", df.groupby(['부서명'])['연봉'].max())
    print("부서별 연봉의 최소 : ", df.groupby(['부서명'])['연봉'].min())
    print()
    print(pd.crosstab(df['부서명'], df['직급'], margins = True))

    # 직원별 담당 고객자료를 출력
    for i in range(1, len(df.index) - 1):
        sql2 = """
            select gogek_no, gogek_name, gogek_tel
            from gogek inner join jikwon 
            on gogek.gogek_damsano = jikwon.jikwon_no
            where jikwon_no = {}
        """.format(str(df.index[i]))

        #print(sql)
        cursor.execute(sql2)
        result = cursor.fetchone()

        if result == None:
            print(df['이름'][i + 1]," : 담당 고객  X")
        else:
            print(df['이름'][i + 1], '직원의 담당고객 정보')
            df2 = pd.read_sql(sql2, conn)
            df2.columns = ['고객번호', '고객명', '전화번호']
            df2.set_index('고객번호', inplace=True)
            print(df2)

    # 부서명별 연봉의 평균으로 가로 막대 그래프
    jik_ypay = df.groupby(['부서명'])['연봉'].mean()
    plt.barh(jik_ypay.index, jik_ypay.values)
    plt.show()
except Exception as e:
    print("err : ", str(e))
finally:
    cursor.close()
    conn.close()