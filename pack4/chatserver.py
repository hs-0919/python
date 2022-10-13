# 멀티 채팅 서버 프로그램 - socket + thread
import socket
import threading


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 5000))
ss.listen(5)
print('채팅 서버 서비스 시작...')

users =[]

def chatUser(conn):     # 스레드 처리 함수 
    name = conn.recv(1024)
    data = '=.=' + name.decode('utf-8')+'님 입장! 메루치보꾸!'
    print(data)
    
    try:
        for p in users:
            p.send(data.encoding('utf-8'))
            
        while True:
            msg = conn.recv(1024)
            if not msg:continue
            data = name.decode('utf-8') + '님 메세지:' + msg.decode('utf-8')
            print('수신 내용 : ', data)
            for p in users:
                p.send(data.encoding('utf-8'))
            
    except:     # 유저가 빠져나가면 에러남
        users.remove(conn)
        data = '^^7' + name.decode('utf-8')+'님 퇴장! 메루치보꾸!'   # 퇴장 했다고 알려주고
        print(data)
        if users:
            for p in users:
                p.send(data.encoding('utf-8')) # 퇴장 했다는 메세지 보냄
        else:
            print('사람이 없어요~')
    
while True:
    conn,addr = ss.accept()  # 계속 기다림 - 승인할때 까지
    users.append(conn)  # 클라이언트를 저장
    th = threading.Thread(target=chatUser, args=(conn,))
    th.start()
    
    
    
    