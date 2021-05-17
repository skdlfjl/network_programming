'''
2. 리스트 ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']에 대해 슬라이싱과
함수(메소드 포함)를 이용하여 아래와 같이 수행하는 프로그램을 작성하라. (10점)
'''
msg = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']

#A. 리스트 마지막에 '!'를 추가한 후 출력하라.
msg.append('!')
print(msg)

#B. 다섯 번째 요소('o')를 제거한 후 출력하라.
del msg[4]
print(msg)

#C. 인덱스 4에 'a'를 넣은 후 출력하라.
msg.insert(4, 'a')
print(msg)

#D. 리스트를 문자열로 변환하여 출력하라.
print(''.join(msg))


#E. 리스트를 오름차순으로 정렬하여 출력하라.
print(sorted(msg, reverse = True))