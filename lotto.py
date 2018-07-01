'''
로또 구입
1장 - 번호 리스트 5개
n장 - 번호 리스트 5n개
1회 최대 20장

모의 로또 추첨
번호 1~45 6개(이미 뽑힌 번호 제외)
보너스 번호 이미 뽑힌 6개 번호 제외한 1~45 1개
'''



import random
import time

# 중복없이 번호 뽑기
'''
lottolists=[]
cope = list(range(1,46))
random.shuffle(cope)
while len(cope)>40:
    p = cope.pop()
    lottolists.append(p)

print(lottolists)
'''

# 로또 구입
while True:
    try:
        howmany = int(input('로또 몇장을 구입하겠습니까?\n'))
    except ValueError:
        print('\n숫자를 정확히 입력해주세요.')
    else:
        if howmany<=20:
            getlotto = 5*howmany
            mylottolist = [[] for j in range(getlotto)]

            for j in range(getlotto):
                lotto_all = list(range(1,46))
                while len(lotto_all)>39:
                    random.shuffle(lotto_all)
                    get_num = lotto_all.pop()
                    mylottolist[j].append(get_num)
            print('\n내가 구입한 로또의 내역은 다음과 같다.\n')
            for each_num in mylottolist:
                each_num.sort()
                print(each_num)
            break
        else:
            print('\n로또의 최대 구입 한도는 20장입니다.\n')

# 모의 로또 추첨
print('''
=====================
    모의 로또 추첨
=====================
''')
time.sleep(1)

while True:
    try:
        YesorNo = int(input('\n모의 로또 추첨을 해보시겠습니까?\n1.예    2.아니오\n'))
    except ValueError:
        print('\n정확한 숫자를 입력하세요.(1 or 2)')
    else:
        if YesorNo == 1:
            lotto_all = list(range(1,46))
            lottolist = []
            n = 5
            while len(lotto_all)>39:
                random.shuffle(lotto_all)
                get_num = lotto_all.pop()
                lottolist.append(get_num)
            lottolist.sort()
            print('\n잠시만 기다려 주세요...')
            time.sleep(2)
            print('\n추첨 번호는 바로!')
            time.sleep(2)
            print(str(lottolist)+'입니다!\n\n행운의 보너스 번호는 과연~?')
            while n>0:
                time.sleep(1)
                print(n)
                n-=1
            bonus = lotto_all.pop()
            print('보너스 번호는 바로! '+str(bonus)+'입니다~')
            result = str(lottolist)+' + '+ str(bonus)
            print('\n최종 모의 로또 추첨 번호는 '+ result +'입니다!\n')

            # 당첨여부 확인
            if lottolist in mylottolist:
                print('와우! 축하합니다! 로또 1등에 당첨됐습니다!!!!')
            else:
                lottolist.append(bonus)
                lottolist.sort()
                for i in range(len(mylottolist)):
                    check_num = [x for x in lottolist if x in set(mylottolist[i])]
                    if len(check_num)>5:
                        print(check_num)
                        print('축하합니다! 2등에 당첨됐습니다!')
                    elif len(check_num)>4:
                        print(check_num)
                        if bonus in check_num:
                            print('축하합니다! 4등에 당첨됐습니다!')
                        else:
                            print('축하합니다! 3등에 당첨됐습니다!')
                    elif len(check_num)>3:
                        print(check_num)
                        if bonus in check_num:
                            print('축하합니다! 5등에 당첨됐습니다!')
                        else:
                            print('축하합니다! 4등에 당첨됐습니다!')
                    elif len(check_num)>2:
                        if bonus in check_num:
                            pass
                        else:
                            print(check_num)
                            print('축하합니다! 5등에 당첨됐습니다!')
        elif YesorNo == 2:
            print('\n로또는 무슨 로또냐~!')
            break
        else:
            print('\n1이나 2를 입력하세요.')
