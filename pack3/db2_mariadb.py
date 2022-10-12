# 원격 데이터베이스 연동 프로그램
# pip install mysqlclient  -> 아나콘다3 프롬트에 입력 -외부라이브러리 설치
import MySQLdb

# conn=MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
# print(conn)
# conn.close()

# sangdata table과 연동하기
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config) ## **dict 타입으로 받음
    # print(conn) - 연결되었나 확인
    cursor = conn.cursor()
    
    '''
    # insert
    # sql = "insert into sangdata(code,sang,su,dan) values(10, '신상1',5,'5000')"
    sql = "insert into sangdata values(%s, %s, %s, %s)"
    sql_data = '11', '아아', 12, '2500'
    
    count = cursor.execute(sql, sql_data)
    print(count) # 성공하면 1 실패하면 0
    conn.commit()
    '''
    
    '''
    # update
    sql = "update sangdata set sang=%s, su=%s where code=%s "
    sql_data = ('파이썬', 50, 11)
    count = cursor.execute(sql, sql_data)
    print(count) # 성공하면 1 실패하면 0
    conn.commit()
    '''
    
    '''
    # delete
    code = '11'
    # sql = "delete from sangdata where code="+code -->> 씨큐어 코딩 가이드라인에 위배된다.
    # sql = "delete from sangdata where code='{0}'".format(code)
    # cursor.execute(sql)
    
    sql = "delete from sangdata where code=%s"
    cursor.execute(sql, (code,))
    conn.commit()
    '''
    
    # select 
    sql = "select code, sang, su, dan from sangdata"
    cursor.execute(sql)
    
    # 방법1
    for data in cursor.fetchall():
        #print(data)
        print('%s %s %s %s'%data)
    
    # 방법2
    print()
    for r in cursor:
        # print(r)
        print(r[0], r[1], r[2], r[3])
    
    # 방법3
    print()
    for (code, sang, su, dan) in cursor:
        print(code, sang, su, dan)
        
    # 방법3-1
    print()
    for (a,품명,su,dan) in cursor:
        print(a,품명,su,dan)
    
    
    
except Exception as e:
    print('err :', e)
finally:
    cursor.close()
    conn.close()
















