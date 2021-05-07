from socket import *
import threading

BUFFSIZE = 1024
server_addr = ('localhost', 9911)

# 뭐든지 recv해서 출력해준다
def recv_(sock):
    while True:
        # 서버의 메인 스레드에서 ID 를 받을수도 있고
        # 서버의 별도 스레드에서 '[ID] 메세지' 를 받을수도 있다
        msg = sock.recv(BUFFSIZE)
        print(msg.decode())

sock = socket()
sock.connect(server_addr)

# 일단 ID는 무조건 처음에 1번 전송해야하니까 while문 밖에 적어준다
my_id = input('ID를 입력하세요: ')
sock.send(('[' + my_id + ']').encode())

while True:  
    # 처음에 ID를 받아야 하니까 채팅을 입력할 input() 위에 써줘야 한다
    th = threading.Thread(target=recv_, args=(sock,))
    th.daemon = True
    th.start()

    # 여기엔 채팅을 입력받아서 서버로 send해주는 부분
    # 입력이 quit 일경우 서버로 전송 후 break 해준다
    data = input()
    sock.send(data.encode())
    if 'quit' == data:
        break

sock.close()