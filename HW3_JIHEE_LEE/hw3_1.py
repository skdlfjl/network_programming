# 1. 아래 내용에 대한 프로그램(1개)을 작성하라.
days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 
'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}

# 사용자가 월을 입력하면 해당 월에 일수를 출력하라.
month = input('please enter a month : ')
print(month, ":", days[month])

# 알파벳 순서로 모든 월을 출력하라.
print(sorted(days))

# 일수가 31인 월을 모두 출력하라.
for key, value in days.items():
    if value == 31:
        print(key, ":", value)

# 월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라.
print(sorted(days.items(), key = lambda t: t[1]))   # 1을 0으로 바꿔주면 월의 알파벳 순서 기준으로 정렬

# 사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
month_3 = input('enter 3 characters of the month : ')
for key in days.keys():
    if month_3 in key:
        print(key, ":", days[key])

