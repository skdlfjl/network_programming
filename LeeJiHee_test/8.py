'''브라우저에서 ‘http://localhost:9000’ 입력

- 릴레이 서버는 해당 메시지를 수신한 후, 외부 서버로 HTTP 요청 전송

∙ HTTP 요청 메시지 전송 시, HTTP 메시지의 요청 라인(GET으로 시작하는 HTTP 헤더의
첫 줄)과 ‘Host: www.daum.net’만 전송하도록 함

- 릴레이 서버는 외부 서버로부터 HTTP 응답을 수신 후, 브라우저에게 전달

- 브라우저는 해당 응답 메시지를 처리 (리다이렉트 후 화면에 보여줌. 우리는 이 부분에
대해 신경 쓸 필요 없음)

'''

from socket import *

#s2 = socket(AF_INET, SOCK_STREAM)
#s2.connect(('localhost', 80))

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000)) # 웹 서버 소켓(port : 80)
s.listen(10)
print('waiting...')

while True:
    c, addr = s.accept() # blocking

    data = c.recv(1024) # HTTP 전체를 읽어들여옴
    if not data: 
        break
    msg = data.decode() # decode
    req = msg.split('\r\n')  # '\r\n' : 엔터

    # print('req :', req)
    # 첫번째 라인(요청라인)은 req[0]에 들어있음을 확인
    
    #s2.send(req[0].encode())
    #s2.send(b'Host: www.daum.net')
    #c.send(b'\r\n')








    c.close()

s.close()