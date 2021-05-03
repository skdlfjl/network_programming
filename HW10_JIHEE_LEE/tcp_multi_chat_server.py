# 채팅 서버는 수신한 메시지를 발신자를 제외한 다른 클라이언트에게 전송
# 채팅 클라이언트가 ‘quit’를 전송하면 해당 클라이언트를 목록에서 삭제

from socket import *
import threading
import time

c_list = []  # 클라이언트 목록(리스트)

port = 9910
BUFFSIZE = 1024


# 스레드에서 실행할 코드를 함수로 구현
def chatting(sock, addr, id):
    # sock은 특정 클라이언트와 연결된 통신 소켓 conn이다.
    while True:
        data = sock.recv(BUFFSIZE)
        # 'quit'를 전송했으면 c_list 안에 'quit'를 보낸 사용자의 소켓을 삭제한다
        if 'quit' in data.decode():
            if sock in c_list:
                print(addr, 'exited')
                c_list.remove(sock)
                break
        # 그냥 메세지 전송한거면 나 빼고 다른 애들의 소켓을 통해 전부 send
        else:
            msg = id + ' ' + data.decode()
            for c_sock in c_list:
                if c_sock != sock:
                    c_sock.send(msg.encode())


# 메인 스레드          
s = socket()
s.bind(('', port))
s.listen(5)
print('Server Started')

while True:
    conn, addr = s.accept()
    print('new client', addr)

    # 새로운 클라이언트일 경우 c_list에 추가해준다
    if conn not in c_list:
        c_list.append(conn)

    # 일단 ID는 무조건 처음에 1번 받아지니까 받아서 id_msg 변수에 저장
    id_msg = conn.recv(BUFFSIZE)
    if not id_msg:
        print('not id_msg')
        break
    # 그리고 당사자를 제외한 접속해있는 사람들에게 id_msg를 send
    for c_sock in c_list:
        if c_sock != conn:
            c_sock.send(id_msg)
    print(time.asctime() + str(addr) + ' : ' + id_msg.decode())


    # 스레드를 생성한다
    th = threading.Thread(target=chatting, args=(conn, addr, id_msg.decode()))
    th.start()

