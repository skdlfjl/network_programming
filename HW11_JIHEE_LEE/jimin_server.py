from socket import *
import select
import time 

#연결되는 소켓을 담을 리스트 
s_list = []

BUFFER = 1024
PORT = 5555

s_sock = socket()
s_sock.bind(('', PORT))
s_sock.listen(10)

s_list.append(s_sock)
print(str(PORT) + " 에서 접속 대기중")


#r_sock :  [<socket.socket fd=412, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 3000)>] 
#읽기가 가능한 리스트의 목록 
#s_sock :  <socket.socket fd=412, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 3000)>
#처음 서버를 연결하면 생기는 소켓 

while True: 
   r_sock , w_sock, e_sock = select.select(s_list, [], [])
   
   for s in r_sock:
        if s== s_sock:
            c_sock, addr = s_sock.accept() 
            s_list.append(c_sock)
            print("Client {} connected".format(addr))
   
        else:    
            data = s.recv(BUFFER)
            if "quit" in data.decode() :
                print(addr, 'exited')
                s_list.remove(s)
                break
         
            else:
                #print(s_list) 
                for i in range(1, len(s_list)):
                    if s_list[i] != s :
                        s_list[i].send(data)
                        print("send complete")
            print(time.asctime() + str(addr) + ": " + data.decode())