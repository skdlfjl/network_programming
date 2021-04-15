'''
1. 사용자로부터 
“send [mboxID] message” or “receive [mboxID]” or “quit” 문자열 입력받음

2. 입력받은 문자열을 서버로 전송
> “quit” 문자열 전송 후, 프로그램 종료

3. 응답으로 받은 문자열을 화면에 출력'''

from socket import *

BUFF_SIZE = 1024
port = 8888

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message(“send [mboxID] message” or “receive [mboxID]”): ')
    sock.sendto(msg.encode(), ('localhost', port))
    if msg == 'quit':
        # print('-> “quit” 메시지를 입력하여 프로그램을 종료합니다 ')
        break
    
    
    data, addr = sock.recvfrom(BUFF_SIZE)
    print('-> ', data.decode())