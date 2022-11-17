# 예외 처리 : 작업 도중 발생하는 에러에 대처하기
# try ~ except

def divide(a, b):
    return a / b 


print('이런 저런 작업을 하다가..')
c= divide(5, 2)
# c= divide(5, 0)  err
print(c)

print()
try:
    #c= divide(5, 2)
    #c= divide(5, 0)
    print(c)
    
    aa=[1,2]
    #print(aa[0])
    #print(aa[5])
    
    open('C:/abc.txt')
    
except ZeroDivisionError:
    print('에러 : 0으로 나누면 안돼')

except IndexError as err:
    print('에러 원인: ', err)
except Exception as e:
    print('기타 에러: ', e)
finally:
    print('에러 유무에 상관없이 반드시 실행')
    
print('프로그램 종료')










