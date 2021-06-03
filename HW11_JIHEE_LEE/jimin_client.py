from socket import *
import time
import threading

port = 5555
BUFFSIZE = 1024


def recv(sock):
    while True:
        msg = sock.recv(BUFFSIZE)
        print(msg.decode())

sock= socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost',port))     

my_id = input("ID를 입력하세요 : ")
sock.send(('[' + my_id + ']').encode())


while True:
    th = threading.Thread(target=recv , args=(sock,))
    th.start()
    
    msg = '[' + my_id + '] ' + input()
    sock.send(msg.encode())
