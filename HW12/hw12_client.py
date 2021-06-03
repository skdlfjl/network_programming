from socket import *
import threading
import time

BUF_SIZE = 1024

# 2개의 IoT 디바이스와 TCP 연결
s1 = socket()
s1.connect(('localhost', 9991))
s2 = socket()
s2.connect(('localhost', 9992))


f = open('data.txt', 'w')
# recv 한 뒤, 시간정보를 추가하여 출력한다
# 그리고 수집한 데이터는 파일에 저장
def recv_(sock):
    while True:
        msg = sock.recv(BUF_SIZE)
        if not msg:
            break
        if 'device2 complete' in msg.decode():
            f.close()
            break
        print(time.ctime(time.time()) + msg.decode())
        f.write(time.ctime(time.time()) + msg.decode() + '\n')
    

# 프로그램이 시작되면, '디바이스 1'과 '디바이스 2'로 'Register' 메시지를 전송
s1.send(b'Register')
s2.send(b'Register')


# while 문을 돌면서 계속해서 thread를 생성하는 것이 문제인 것 같습니다.
# thread는 한번만 생성하면 되므로, 아래와 같이 코드 수정하였습니다.
th1 = threading.Thread(target=recv_, args=(s1,))
th2 = threading.Thread(target=recv_, args=(s2,))

#th1.daemon = True
#th2.daemon = True

th1.start()
th2.start()

th1.join()
th2.join()



