from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 6666))
print('Ex) 20 + 17')

def changeStr(str_num):
    if '.' in str_num:
        return float(str_num)
    else:
        return int(str_num)

while True: 
    # 사용자로부터 “20 + 17” 형태의 계산식을 입력 받음
    formula = input('Please enter a mathematical formula: ')
    if formula == 'q': 
        break # 사용자가 “q”를 입력하면 종료

    s.send(formula.encode()) # 입력받은 계산식 서버로 전송

    bytes_str_result = s.recv(1024) # 서버로부터 받은 결과 저장 (바이트형태)
    if not bytes_str_result:
        break
    # from_bytes에 float이 들어갈 수 없으므로 아래랑 다른방법으로 해야함
    # result = int.from_bytes(bytes_result, 'big')

    str_result = bytes_str_result.decode() # 일단 decode만 해준다
    try:
        print('Calculation result: ', changeStr(str_result)) 
        # 소수점이 들어있으면 float, 안들어있으면 int로 print
    except:
        print('Warning: ', str_result) # 'Try again'

s.close()



