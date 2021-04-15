from socket import *
from collections import defaultdict

BUFF_SIZE = 1024
port = 8888

s = socket(AF_INET, SOCK_DGRAM)  # UDP
s.bind(('', port))  # bind()만 해주면 됨
print('Listening...')

dic = defaultdict(list)
# 딕셔너리를 리스트로 디폴트를 바꿈으로써, 리스트 함수를 사용할 수 있게 함

while True:
    data, addr = s.recvfrom(BUFF_SIZE) # 데이터와 주소를 받는다
    # print('전달받은 데이터: ', data.decode())  # 확인용 코드
    msg = data.decode()
    msg_list = msg.split(' ', maxsplit=2)

    if 'send' == msg_list[0]:
        # "send [mboxID] message" 메시지 수신시 
        # [mboxID]에 message를 저장
        dic[msg_list[1]].append(msg_list[2]) 
        print(dic) # 저장 잘 된건지 확인해보기     
        s.sendto(b'OK', addr)  # 저장한 뒤, “OK”를 클라이언트로 전송

    elif 'receive' == msg_list[0]:
        # “receive [mboxID]” 메시지 수신 시            
        # [mboxID]의 제일 앞에 있는 메시지를 클라이언트로 전송 후 삭제  
        try:
            # msg_list[1] == [mboxID]
            # dic[msg_list[1]] == dic에서 [mboxID]의 value(list)를 가져옴
            recv_msg = dic[msg_list[1]][0] # 그 중 첫번째니까 [0]
            s.sendto(recv_msg.encode(), addr)  # 클라이언트로 전송
            # 이제 삭제합시다
            del dic[msg_list[1]][0]
            print(dic) # 삭제된지 확인해보기
        except:
            # 존재하지 않는 [mboxID]나 메시지가 없는 [mboxID]에 대해 
            # “No messages”를 클라이언트로 전송
            print('No messages')
            s.sendto(b'No messages!!', addr)


    elif 'quit' == msg_list[0]:
        # 클라이언트로부터 “quit” 메시지 수신 시, 프로그램 종료
        print('quit')
        break

    else:
        # 오타가 존재하는 경우
        print('Try again')
        s.sendto(b'Try again', addr)

    





