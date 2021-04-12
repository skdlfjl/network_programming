from socket import *

s = socket()
s.bind(('', 80)) # 웹 서버 소켓(port : 80)
s.listen(10)
print('waiting...')

while True:
    c, addr = s.accept() # blocking

    data = c.recv(1024) # HTTP 전체를 읽어들여옴
    if not data:  # 여기에도 써야하는건가??
        break
    msg = data.decode() # decode
    req = msg.split('\r\n')  # '\r\n' : 엔터

    print('req[0] :', req[0])
    # 첫번째 라인(요청라인)은 req[0]에 들어있음을 확인
    # /index.html을 파싱하기 위해 ' ' 기준으로 split 해준 뒤, 인덱스 사용
    filename = req[0].split(' ')[1] 
    
    if '/' in filename:
        filename = filename.replace('/','') # '/'가 있는경우, 제거하여 파일이름 얻기

    print(filename)

    try:
        if filename == 'index.html':
            f = open(filename, 'r', encoding = 'utf-8')
            mimeType = 'text/html'

        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png' 

        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'

        # HTTP Response 메세지
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        data = f.read() # index.html 파일을 읽는다
        
        if filename == 'index.html':
            c.send(data.encode('utf-8'))  # 혹은 c.send(data.encode())
            #c.send(data.encode('euc-kr')) # ???????????
        else:
            c.send(data)
        print(filename, 'send success!!')


    except:
        # Not Found HTTP Response 메세지
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
        print('Not Found')


    c.close()

s.close()