'''
5. 강의자료 “소켓 프로그래밍 (UDP)”에서 슬라이드 
11, 12, 13의 “과제 8: UDP message 송수신 프로그램”을 
TCP를 이용하여 구현하라

주의사항 
- 서버는 quit을 수신한 후, 연결을 종료하지 않고 다음 클라이언트의 
연결을 기다려야 함

- 서버와 클라이언트의 소스 코드를 모두 제출해야 함

'''

from socket import *
from collections import defaultdict

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)

BUFF_SIZE = 1024
dic = defaultdict(list)

while True:
    c, addr = s.accept()
    print('connection', addr)

    while True:
        data = c.recv(BUFF_SIZE)
        if not data:
            break
        msg = data.decode()

        m_list = msg.split(' ', 2)

        if m_list[0] == 'send':
            dic[m_list[1]].append(m_list[2])
            print(dic)
            c.send(b'OK')

        if m_list[0] == 'receive':
            try:
                msg = dic[m_list[1]][0]
                print(msg)

            except:
                c.send(b'No messages')

            else:
                c.send(msg.encode())
                del dic[m_list[1]][0]
                print(dic)

        if m_list[0] == 'quit':
            break

    c.close()

s.close()

