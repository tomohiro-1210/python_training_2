#演習①
x = 15
if x >= 10 and x <= 20:
    print('xの値は' + str(x) + 'で、10以上20以下')
else:
    print('それ以外')

#演習②
kokugo = 40
sugaku = 100

if kokugo + sugaku >= 140:
    if kokugo <= 60 or sugaku <= 60:
        print('不合格')
    else:
        print('合格')
else:
    print('不合格')

# 演習③
user_point = 5000
acquisition_times = 40
has_card = True

judge_point = user_point >= 4000
judge_times = acquisition_times >= 30
judge_card = has_card == True

if judge_point and judge_times and judge_card:
    print("ダイヤモンド会員です")
elif user_point >= 2000 and acquisition_times >= 15:
    print("プラチナ会員です")
elif user_point >= 700 and acquisition_times >= 7:
    print("コールド会員です")
else:
    print("シルバー会員です")