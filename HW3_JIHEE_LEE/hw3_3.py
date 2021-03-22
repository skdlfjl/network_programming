'''3. 다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수를 포함하는 프로그램을 작성하라.

예) 문자열 'led=on&motor=off&switch=off'이고 구분 문자가 '&', '='일 때 {'led':'on', 'motor':'off', 'switch':off'} 반환 '''

str = input('ex) led=on&motor=off&switch=off : ')
str_dict = {}

str_list = str.split('&')
for i in str_list:
    str_dict[i.split("=")[0]] = i.split("=")[1]  
print(str_dict)

