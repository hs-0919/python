# 개인용 DB : sqlite3 : 파이썬 기본 개인용 데이타베이스

import sqlite3
print(sqlite3.sqlite_version)

print()
#conn = sqlite3.connect('exam.db')
conn = sqlite3.connect(':memory:') # ram에 일시적으로 데이터가 저장된다 - 테스트용으로 사용한다.
try:
    
    cursor = conn.cursor() # SQL문 처리는 커서로

    # 테이블 생성 - SQL문 가급적 큰따옴표 "" 로 쓰자
    cursor.execute("create table if not exists fritab(name text, phone text)")
    
    # 자료 추가
    cursor.execute("insert into fritab(name,phone) values('한국인','1111-1111')")
    cursor.execute("insert into fritab values('우주인', '121-1221')")
    cursor.execute("insert into fritab values('외국인', '131-1331')")
    cursor.execute("insert into fritab values(?,?)", ('단풍이', '141-1441'))
    inputdata= ('커피집', '444-1111')
    cursor.execute("insert into fritab values(?,?)", inputdata)
    conn.commit()
    
    # select
    cursor.execute("select * from fritab")
    print(cursor.fetchone())
    print(cursor.fetchall())
    
    
    
    
    
except Exception as e:
    print('오류 :', e)
    conn.rollback()

finally:
    conn.close()

