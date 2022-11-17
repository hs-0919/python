# Maria DB 연결정보를 객체로 저장

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

import pickle

with open('mydb.data', mode='wb') as obj:
    pickle.dump(config, obj)
    
# mydb.data가 만들어졌습니다... 






