# 여러 스레드 간 공유자원 충돌 방지
# 동기화(줄서기) - 하나의 스레드가 자원을 사용하는 동안 다른 스레드는 공유자원사용을 대기

import threading, time 
g_count = 0  # 전역변수는 자동으로 스레드의 공유자원이 된다.(충돌이 일어날 수 있다)
lock = threading.Lock()


def threadCount(id, count):
    global g_count
    for i in range(count):
        lock.acquire()   # 스레드 간 충돌 방지용, 현재 스레드가 공유자원을 점유하고 있는 동안 다른 스레드는 대기 상태에 있는거
        print('id : %s ===> count : %s, g_count : %s'%(id, i, g_count))
        time.sleep(0.1)
        g_count += 1
        lock.release()   # 공유자원을 점유 해제
        
        
for i in range(1,6):
    threading.Thread(target=threadCount, args=(i, 5)).start()  # 5 -> 5번 돌린다 (랜덤하게 5번돈다)


time.sleep(5)
print('처리 후 최종 g_count :', g_count)
print('프로그램 종료')


