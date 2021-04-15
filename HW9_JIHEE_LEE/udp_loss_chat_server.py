from socket import *
import random
import time

port = 9999
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    # None은 타임아웃 없이 계속 기다림(무한정 블로킹)
    sock.settimeout(None) # 채팅 메세지를 기다리는 부분!
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE) # 채팅 메세지 받음(수신)
        if random.random() <= 0.5:
            continue  # 50%확률로 13번째 줄로 돌아간다(의도적 데이터 손실)
        else:
            sock.sendto(b'ack', addr) # 50%확률로 잘 받은 경우 ack전송
            print('<-', data.decode()) # 받은 채팅 메세지 출력
            break # 잘 받았으니까, break로 빠져나간다
    
    # 이제 서버에서 클라이언트로 보낼거임
    msg = input('-> ')
    reTx = 0  # 한번에 잘 보내지면 채팅 메세지 앞에 0이 붙는다
    while reTx <= 3:  # 재전송 횟수 3번 (0, 1, 2, 3 == 총 4번)
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)  # 타임아웃 시간 2초
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            # 2초동안 'ack'을 못받으면 타임아웃 발생
            reTx += 1  # 재전송 횟수 reTx를 1 증가시키고 
            continue   # 27번째 줄로 돌아가서 재전송
        else:
            break  # 'ack'을 잘 받음, break로 빠져나간다
