# 사용자로부터 ‘Register’ 메시지를 수신하면 
# 온도, 습도, 조도를 3초마다 주기적으로 전송
from socket import *
import selectors
import random
import time

port = 9991
BUF_SIZE = 1024

sel = selectors.DefaultSelector() # 이벤트 처리기(셀렉터) 생성

# 새로운 클라이언트로부터 연결을 처리해주고 (accept())
# 새로운 소켓(conn)을 감시하도록 하는 함수
def accept(sock, mask):   # mask는 어떤 이벤트가 발생했나?
    conn, addr = sock.accept()
    print('Client ({}) connected',format(addr))
    sel.register(conn, selectors.EVENT_READ, read)
    # 클라이언트 소켓(conn)을 이벤트 처리기에 등록 
    # (이벤트 read를 감시할거야~) 이벤트 발생시 read() 호출함

# 기존 클라이언트로부터 수신한 데이터를 처리하는 함수
def read(conn, mask):
    data = conn.recv(BUF_SIZE)
    if not data:
        sel.unregister(conn)    # 소켓 연결 종료시 이벤트 처리기에서 등록 해제
        conn.close()
        return
    
    # 사용자로부터 'Register' 메세지를 수신한 경우
    elif data == b'Register':
        for i in range(5):  # 5번 전송
            #c_time = time.ctime(time.time()) # 클라이언트가 접속한 시간
            tem = str(random.randint(0, 40))   # 온도
            hum = str(random.randint(0, 100))  # 습도
            ill = str(random.randint(70, 150)) # 조도
                
            msg = ': Device1 : Temp = ' + tem + ', Humid = ' + hum + ', Iilum = ' + ill
            print(msg)
            conn.send(msg.encode())
            time.sleep(3) # 보내고 3초 쉰다
        print('device1 complete')
        #conn.send(b'device1 complete')


sock = socket()
sock.bind(('', port))
sock.listen(5)
print(str(port) + '(device1)에서 접속 대기중')


# 서버소켓을 이벤트 처리기에 등록
# read(recv)이벤트 발생하면 accept라고 알려줘!
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    # select()객체를 호출해서 블로킹 되어 기다림 (이벤트 발생시 알려준다)
    events = sel.select()  # 등록된 서버소켓에 대한 이벤트 감시 시작!

    # 발생한 이벤트는 여러개일 수 있으니 무조건 for문으로 돌아야됨
    for key, mask in events:    # 발생한 이벤트를 모두 검사
        # 이때, key에는 accept함수 이름이 들어있다.
        callback = key.data     # key.data: 이벤트 처리기에 등록한 함수
        # 아래는 key.data를 그대로 받아서 함수호출 하는것!
        # 즉 callback(key.fileobj, mask) == accept(key.fileobj, mask)
        callback(key.fileobj, mask)   # key.fileobj: 이벤트가 발생한 소켓
