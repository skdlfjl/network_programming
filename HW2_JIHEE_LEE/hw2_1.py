'''
1. 다음과 같은 게임 프로그램을 작성하라.

● 플레이어가 처음에 $50을 가지고 있다. 동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다. 
맞추면 $9을 따고 틀리면 $10을 잃는다. 플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다. '''

from random import randint
player = 50

while True:
    pred = int(input('coin prediction 1 or 2 : '))
    coin = randint(1,2) # 1 또는 2를 임의로 발생

    if coin == pred:
        player = player + 9
        print("$", player, "맞췄습니다.")
    else:
        if player >= 10:
            player = player - 10
        else:
            player = 0
        print("$", player, "틀렸습니다")

    if player == 100:
        print('$100가 되어 게임이 종료됩니다.')
        break
    elif player == 0:
        print('돈을 모두 잃어 게임이 종료됩니다.')
        break

    
