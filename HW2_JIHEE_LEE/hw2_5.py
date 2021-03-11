'''
5. for 루프를 이용하여 다음과 같은 리스트를 생성하라.

● 0~49까지의 수로 구성되는 리스트
● 0~49까지 수의 제곱으로 구성되는 리스트'''

num_list = []
squ_list = []

for i in range(50):
    num_list.append(i)
    squ_list.append(i**2)

print('0~49까지의 수로 구성되는 리스트 : ', num_list)
print('0~49까지 수의 제곱으로 구성되는 리스트 : ', squ_list)
