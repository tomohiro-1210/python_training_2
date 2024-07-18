#　比較演算子
# ==：同じか
print(1 == 1)
print('true' == 'true')
print('yakumo' == 'nanpu' )

# !=:そうでないか
print('a' != 'a')
print(80 != 100)

# is
a = "岡山１１５系４両編成"
b = "網干２２１系６両編成"
print(a is "網干２２１系８両編成")
print(b is "網干２２１系６両編成")

# id
print(id(a)) #aで設定した文字列にIDが入っている。
print(id(b))
print(id("ミミック")) #ミミックもIDが設定されるのか///

# is not
print(a is not b)
print(b is not "網干２２１系６両編成")

#in
text = "なんと宝箱はミミックだった！"
print("なんと" in text)
total = "なんと" in text
print("変数代入:" , total)

#比較の連鎖
num_1 = 100
print(0 <= num_1 <= 200)
num_2 = 30
print(50 <= num_2 <= 100)
print(0 <= num_2 <= 100 <= num_1 <= 150)