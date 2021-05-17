from socket import *

s = socket(AF_INET, SOCK_STREAM)

BUFF_SIZE = 1024
addr = ('localhost', 8888)

s.connect(addr)

while True:
    msg = input('"send [mboxID] message" or "receive [mboxID]" :')
    if msg == 'quit':
        s.sendto(msg.encode(), addr)
        break

    s.send(msg.encode())  # 전송

    data = s.recv(BUFF_SIZE)
    msg = data.decode()
    print(msg)

s.close()
