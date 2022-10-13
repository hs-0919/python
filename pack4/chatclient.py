# 채팅 클라이언트

import socket
import threading
import sys

def handle(socket):
    while True:
        data = socket.recv(1024)
        if not data:continue
        print(data.decode('utf-8'))
        
sys.stdout.flush()   # 파이썬의 표준 출력은 버퍼링이 되는데 이 때 버퍼를 비우기

name = input('채팅 아이디 입력: ')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('192.168.0.7', 5000)) # 챗서버의 while문 만난다
cs.send(name.encode('utf-8'))

th = threading.Thread(target=handle, args=(cs, ))
th.start()

while True:
    msg = input()  # 나도 메세지 보내기
    sys.stdout.flush()
    if not msg:continue
    cs.send(msg.encode('utf-8'))
    
cs.close()
