from socket import *
import select
import threading
import time

c_list = []  # 클라이언트 목록(소켓 리스트)
id_list = []  # [(소켓, ID), ...]

port = 9911
BUFFSIZE = 1024
       
s_sock = socket()
s_sock.bind(('', port))
s_sock.listen(5)

c_list.append(s_sock)  # 소켓 리스트에 서버 소켓을 추가
print(str(port) + '에서 접속 대기 중')

while True:
    # 읽기 이벤트 (연결요청 및 데이터수신) 대기
    r_sock, w_sock, e_sock = select.select(c_list, [], [])

    for s in r_sock:
        # 만약 새로운 클라이언트의 연결 요청 이벤트가 발생할 경우
        # accept()해주고, 연결된 클라이언트 소켓으로부터 ID를 받아온 뒤
        # 연결된 클라이언트 소켓과, 해당 클라이언트 ID를 튜플(혹은 리스트?) 
        # 형태로 저장하고 리스트에 추가 >> id_list
        #
        # 근데 select를 써야하니까 소켓만 저장한 리스트도 만들어야됨 >> c_list
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            print('Client ({}) connected'.format(addr))
            c_list.append(c_sock)

            # 일단 ID는 무조건 처음에 1번 받아지니까 받아서 id_msg 변수에 저장
            id_msg = c_sock.recv(BUFFSIZE)
            if not id_msg:
                print('not id_msg')
                break
            # Fri May  7 15:33:47 2021('127.0.0.1', 49272) : [이지희] 이렇게 찍어주기
            print(time.asctime() + str(addr) + ' : ' + id_msg.decode())
            
            # 그리고 당사자를 제외한 접속해있는 사람들에게 id_msg를 send
            # 이때, c_list 안에 있는 0번째 소켓은 서버소켓이다
            # 그러니까 c_list[0]번째를 제외하고, 나머지 소켓들에게만 send              
            for i in range(1, len(c_list)):
                    if c_list[i] != c_sock:
                        c_list[i].send(id_msg)
            #for c in c_list:
            #    if c != c_sock:
            #        c.send(id_msg)

            # 이렇게 얻은 소켓과 그의 아이디를 튜플 형태로 저장해주자
            c_tupple = (c_sock, id_msg)
            id_list.append(c_tupple)


        # 기존 클라이언트의 데이터 수신 이벤트가 발생할 경우
        else:
            data = s.recv(BUFFSIZE)
            if not data:
                s.close()
                c_list.remove(s)
                continue
            #print('Received:', data.decode())

            # 'quit'를 전송했으면 c_list 안에 'quit'를 보낸 사용자의 소켓을 삭제한다
            if 'quit' in data.decode():
                if s in c_list:
                    print(addr, 'exited')
                    c_list.remove(s)
                    break
            
            # 그냥 메세지를 전송한거면 나 빼고 다른 애들의 소켓을 통해 전부 send
            else:
                for i in range(len(id_list)):
                    if s == id_list[i][0]:
                        msg = id_list[i][1].decode() + ' ' + data.decode()
                        #print(msg)
                # 이때, c_list 안에 있는 0번째 소켓은 서버소켓이다
                # 그러니까 c_list[0]번째를 제외하고, 나머지 소켓들에게만 send        
                for i in range(1, len(c_list)):
                    if c_list[i] != s:
                        c_list[i].send(msg.encode())
                

                # 아래와 같은 방법으로 하면 이상하게 2명이서 대화하다가
                # 다른 한명이 더 들어오면 그 사람이 연결이 안된다
                # 왜 그런걸까?????
                #if c_list[0] == s_sock:
                #    c_list.pop(0)
                #for c_sock in c_list:
                #    if c_sock != s:
                #        c_sock.send(msg.encode())


