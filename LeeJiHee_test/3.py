'''3. 문자열
'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'가
주어졌을 때, 아래 출력 결과와 같이 딕셔너리를 생성한 후 출력하는 프로그램을 작성하라.
'''

msg = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

msg_list = msg.split('?')[1].split('&')

dic = {}
for i in msg_list:
    dic[i.split('=')[0]] = i.split('=')[1]

print(dic)