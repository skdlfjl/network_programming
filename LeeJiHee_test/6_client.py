import socket

port = 5566
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


msg = input('Enter a message: ')
if msg == 'q':
    sock.close()

reTx = 0
while reTx <= 3:
    while True:
        sock.sendto(msg.encode(), ('localhost', port))
        print('{}번째 전송'.format(reTx))
        sock.settimeout(1)
        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except socket.timeout:   # from socket import * 가 아니라서!
            reTx += 1
            continue
        else:
            print(data.decode()) #ack
            msg, addr = sock.recvfrom(BUFFSIZE)
            print('Server says: ', msg.decode())
    


sock.close()