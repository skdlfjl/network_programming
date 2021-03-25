import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9872)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

# 본인의 이름을(JiHee Lee) 문자열로 전송
sock.send(b'JiHee Lee')

# 본인의 학번을 수신 후 출력 
bytes_num = sock.recv(1024)
num = int.from_bytes(bytes_num, 'big')
print(num)


sock.close()

