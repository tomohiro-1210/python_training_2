#比較演算子を使った例
score_en = 90
score_ma = 60
score_ja = 30
score_sc = 70
score_hi = 100
score_total = score_en + score_ma + score_ja + score_sc + score_hi
score_len = [score_en, score_ma, score_ja, score_sc, score_hi]

for score_solo in score_len:
    if score_solo >= 40:
        print(str(score_solo) + '点なので合格')
    else:
        print(str(score_solo) + '点なので赤点')

if score_total <= 200:
    print('総合得点の結果は：不合格')
else:
    print('総合得点の結果は：合格')

# 例その２
is_food = True
take_out = False

if is_food and take_out:
    print('税率8％')
else:
    print('税率10%')

# 例その３
string = ''
if string:
    print(f'string is {string}')
else:
    print('string is empty')

# ifの中にif
age = 7
gender = 'male' #maleは男の子,femaleは女の子

if gender == 'female':
    if age == 7:
        print('7歳の女の子です')
    elif age == 5:
        print('5歳の女の子です')
    elif age == 3:
        print('3歳の女の子です')
else:
    if age == 7:
        print('7歳の男の子です')
    elif age == 5:
        print('5歳の男の子です')
    elif age == 3:
        print('3歳の男の子です')

