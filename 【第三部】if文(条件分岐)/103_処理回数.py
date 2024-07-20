#ifの判定
rate = 0.795
if rate >= 0.8:
    print('黒い傘を持っていっている')
elif rate >= 0.4 and rate <= 0.79:
    print('折り畳み傘はあった方がいいね')
else:
    print('念のため傘を持っていている')

#入れ子になっている場合
a = -10
b = -5

if a > b:
    print('aはbより大きいです')

    if a > 15:
        print('aは15より大きいです')
    elif a > 12:
        print('aは12より大きいです')
    else:
        print('aは12以下です')

else:
    print('aはbより小さいです')

    if b < 0:
        print('bは負の値です')
    else:
        print('bは正の値です')