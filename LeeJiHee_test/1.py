'''
1. 문자열 'Hello, IoT'에 대해 슬라이싱과 함수(메소드 포함)를 이용하여 아래와 같이
수행하는 프로그램을 작성하라. (10점)
'''
msg = 'Hello, IoT'

#A. 문자열의 문자수를 출력하라.
print(len(msg))

#B. 문자열을 5번 반복한 문자열을 출력하라.
print(msg*5)

#C. 문자열의 처음 3문자를 출력하라.
print(msg[:3])

#D. 문자열의 마지막 3문자를 출력하라.
print(msg[-3:])

#E. 문자를 모두 대문자로 변경하여 출력하라.
print(msg.upper())