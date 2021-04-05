# 클라이언트로부터 계산식을 수신한 후, 결과를 반환
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 6666))
s.listen(2) # 2명만 동시접속
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break

        formula = data.decode()
        f_list = formula.split(' ')

        try:
            if f_list[1] == '+':
                result = int(f_list[0]) + int(f_list[2])
            elif f_list[1] == '-':
                result = int(f_list[0]) - int(f_list[2])
            elif f_list[1] == '*':
                result = int(f_list[0]) * int(f_list[2])
            elif f_list[1] == '/':
                # 소수점 1자리까지 표기 (반올림)
                result = round(int(f_list[0]) / int(f_list[2]), 1)
        except:
            client.send(b'Try again') # 띄어쓰기 안하면 출력됨
        else:
            # to_bytes에 float를 사용할 수 없으므로 아래랑 다른방법으로 해야함
            # bytes_result = (result).to_bytes(4, 'big')
            # client.send(bytes_result)
            
            bytes_str_result = str(result).encode()  # 문자열로 바꿔주고 encode
            client.send(bytes_str_result)  # 그 상태로 전송한다
    
    client.close()
s.close()



