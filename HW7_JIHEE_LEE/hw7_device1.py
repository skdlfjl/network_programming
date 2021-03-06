from socket import *
import random
import time

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7771))
sock.listen(3)
print('device1 waiting...')

while True:
    try:
        conn, addr = sock.accept()
        while True:
            msg = conn.recv(BUF_SIZE)  # 1024
        
            # not msg일 경우 종료!
            if not msg:
                conn.close()
                continue

            # 만약 받은 메세지가 'quit'일 경우 종료!
            elif msg == b'quit': 
                print('client:', addr, msg.decode())
                conn.close()
                continue

                # 받은 메세지가 'Request'일 경우
            elif msg == b'Request':
                print('client:', addr, msg.decode())
                conn.send(b'Successful Request!')
                conn.send(time.ctime(time.time()).encode()) # 클라이언트가 접속한 시간 전송


            # 받은 메세지가 'Request'가 아닐 경우 되돌아가기
            else:
                print('client:', addr, msg.decode())
                conn.send(b'Try again')
                continue
        
        
            tem = random.randint(0, 40)   # 온도
            hum = random.randint(0, 100)  # 습도
            ill = random.randint(70, 150) # 조도
            msg = '{0} {1} {2}'.format(tem, hum, ill)
            # print(msg)
            conn.send(msg.encode()) # "온도 습도 조도" 메세지 전송

    except:
        continue

    conn.close()
sock.close()
