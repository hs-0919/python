# file i/o

import os
print(os.getcwd())  # 현재 절대 경로 알아내기

try:
    print('파일 읽기~~~~~~~~')
    
    
    #f1 = open(r'C:\work\psou\pro1\pack3\file_test.txt', mode='r', encoding='utf8')
    f1=open('file_test.txt', mode='r', encoding='utf8')
    # mode= 'r', 'w', 'a', 'b', ....
   
    print(f1)
    print(f1.read())
    f1.close() #파일을 열었으면 닫아줘
    
    print('저장----')
    f2 = open('file_test2.txt', mode='w', encoding='utf-8')
    f2.write('My friends\n')
    f2.write('최프로, 식사는 잘 잡솼나?')
    f2.close()
    
    print('추가----')
    f3 = open('file_test2.txt', mode='a', encoding='utf-8')
    f3.write('\n정프로')
    f3.write('\n정프로, 식사는 잘 잡솼나?')
    f3.close()
    
    print('읽기----')
    f4 = open('file_test2.txt', mode='r', encoding='utf-8')
    print(f4.readline())
    
    
except Exception as e:
    print('에러 : ', e)