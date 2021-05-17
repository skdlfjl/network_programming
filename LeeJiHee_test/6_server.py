'''
6. 강의자료 “소켓 프로그래밍 (UDP)”에서 슬라이드 3, 4의 “UDP 에코 서버/클라이언트
프로그램”에 아래와 같이 손실 복구 기능을 추가하라. (15점)
'''

# 손실은 클라이언트에서 서버로 보내는 경우에만 발생한다고 가정
# 서버는 40%의 확률로 응답하지 않아 손실을 발생시킴. 60%에 대해서는 ‘ack’을 전송
# 클라이언트는 서버로부터 ‘ack’을 받지 못하는 경우, 재전송 수행. 
# 1초 간격으로 최대 3회 재전송 (최초 메시지 포함 최대 4번 전송)

import socket
import random

port = 5566
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    if random.randint(1, 10) <= 4:
        print('40%의 확률로 응답하지 않아 {} lost'.format(addr))
        continue
    print('{} : {}'.format(addr, msg.decode()))   
    sock.sendto(b'ack', addr)   # 나머지 60% 확률로 ack전송
    print('Received: ', msg.decode())
    
    sock.sendto(msg, addr)