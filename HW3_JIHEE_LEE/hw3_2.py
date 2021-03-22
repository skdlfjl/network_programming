# 2. 아래 내용에 대한 프로그램(1개)을 작성하라.
d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''}, {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

# 전화번호가 8로 끝나는 사용자 이름을 출력하라.
print('전화번호가 8로 끝나는 사용자 이름 >>')
for i in d:
    a = list(i.values())
    if '8' in a[1]:
        print(a[0])

# 이메일이 없는 사용자 이름을 출력하라.
print('이메일이 없는 사용자 이름 >>')
for i in d:
    a = list(i.values())
    if '' == a[2]:
        print(a[0])

# 사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라
name = input('please enter user name : ')

names = []
d_list = []
for i in d:
    d_list.append(list(i.values()))
    a = list(i.values())
    names.append(a[0])

if name in names:
    print(d_list[names.index(name)])
else :
    print("이름이 없습니다.")
