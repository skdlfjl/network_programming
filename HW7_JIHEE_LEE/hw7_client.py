from socket import *
import sys

BUF_SIZE = 1024

s1 = socket(AF_INET, SOCK_STREAM)
s1.connect(('localhost', 7771))
s2 = socket(AF_INET, SOCK_STREAM)
s2.connect(('localhost', 7772))

print('1 : device1, 2 : divice2')
f = open('data.txt', 'w')

while True:
    msg = input('Please enter 1 or 2: ')

    if msg == '1':
        s1.send(b'Request')
        r_msg = s1.recv(BUF_SIZE)
        if not r_msg:
            break
        else:
            r_msg = r_msg.decode()

        if r_msg == 'Try again':
            print(r_msg)
            continue
        else:
            # print(r_msg)
            time_msg = s1.recv(BUF_SIZE)
            if not time_msg:
                s1.close()
                sys.exit()     # 브레이크로 바꿔도 되나?????
            else:
                time = time_msg.decode()
                # print(time)

        data_msg = s1.recv(BUF_SIZE)
        if not data_msg:
            s1.close()
            sys.exit()
        else:
            data = data_msg.decode()
            data_list = data.split(' ')
            print(time + ': Device1 : Temp = ' + data_list[0] + ', Humid = ' + data_list[1] + ', Iilum = ' + data_list[2])
            f.write(time + ': Device1 : Temp = ' + data_list[0] + ', Humid = ' + data_list[1] + ', Iilum = ' + data_list[2] + '\n')

    elif msg == '2':
        s2.send(b'Request')
        r_msg = s2.recv(BUF_SIZE)
        if not r_msg:
            break
        else:
            r_msg = r_msg.decode()

        if r_msg == 'Try again':
            print(r_msg)
            continue
        else:
            # print(r_msg)
            time_msg = s2.recv(BUF_SIZE)
            if not time_msg:
                s2.close()
                sys.exit()     # 브레이크로 바꿔도 되나?????
            else:
                time = time_msg.decode()
                # print(time)

        data_msg = s2.recv(BUF_SIZE)
        if not data_msg:
            s2.close()
            sys.exit()
        else:
            data = data_msg.decode()
            data_list = data.split(' ')
            print(time + ': Device2 : Heartbeat = ' + data_list[0] + ', Steps = ' + data_list[1] + ', Cal = ' + data_list[2])
            f.write(time + ': Device2 : Heartbeat = ' + data_list[0] + ', Steps = ' + data_list[1] + ', Cal = ' + data_list[2] + '\n')

    elif msg == 'quit':
        s1.send(msg.encode())
        s2.send(msg.encode())
        print('exit')
        f.close()
        break
        
    else:
        print('Not 1 or 2! Please enter "quit" to exit.')
        continue