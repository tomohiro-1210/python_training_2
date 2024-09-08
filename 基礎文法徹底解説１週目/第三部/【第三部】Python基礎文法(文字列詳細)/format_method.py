train1 = "南風"
train2 = "しまんと"
print('次の特急列車は{}号と{}号の連結です。'.format(train2, train1))

# 数字で位置を指定する方法
kyushu_1 = "かもめ"
kyushu_2 = "みどり"
kyushu_3 = "ハウステンボス"

kyushu_total = "{2}, {0}, {1}"
print(kyushu_total.format(kyushu_1, kyushu_2, kyushu_3))

# 変数で位置を指定する
liella_1 = "かのん"
liella_2 = "クゥクゥ"
liella_3 = "ちさと"
liella_4 = "ギャラクシー"
liella_5 = "はづき"

liella_menber = "{kanon}, {kuku}, {chisato}, {galaxy}, {haduki}"
print(liella_menber.format(
    kanon = liella_1,
    kuku = liella_2,
    chisato = liella_3,
    galaxy = liella_4,
    haduki = liella_5
))

