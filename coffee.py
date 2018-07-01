'''
기획- 커피자판기
가격 - 300
개수 - 10잔
'''


import time

print('''
길을 가다 커피자판기를 발견했다!


-----------------
|   커피자판기   |
-----------------
|  커피 - 300원  |
=================
''')
time.sleep(1)

coffee = 10
while coffee>0:
    try:
        YesorNo = int(input('커피를 마시겠습니까?\n1.예   2.아니오\n'))
    except ValueError:
        print('\n숫자를 정확히 입력하세요.\n')
        pass
    else:
        if YesorNo == 1:
            while True:
                try:
                    money = int(input('\n금액을 넣어주세요. '))
                except ValueError:
                    print('\n금액을 숫자로 넣으세요.\n')
                    pass
                else:
                    if money>300:
                        print('\n커피가 나왔습니다.')
                        print('거스름 돈은 {}원 입니다.'.format(money-300))
                        coffee-=1
                        print('남은 커피는 {}잔 입니다.'.format(coffee))
                    elif money == 300:
                        print('\n커피가 나왔습니다.')
                        coffee-=1
                        print('남은 커피는 {}잔 입니다.'.format(coffee))
                    else:
                        print('금액이 부족합니다.\n남은 커피는 {}잔 입니다.'.format(coffee))
                    if not coffee:
                        print('\n커피가 다 떨어졌습니다.')
                        break
        elif YesorNo == 2:
            print('\n가던 길이나 가기로 했다...')
            break
        elif YesorNo != 1 or 2:
            print('\n1이나 2를 입력하세요.\n')
