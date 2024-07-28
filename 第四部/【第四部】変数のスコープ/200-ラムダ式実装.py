#引数に1を足す
def add_one(x):
    return x + 1

print(add_one(1))
add_one = lambda x: x + 1
print(add_one(2))

add = lambda a ,b : a + b
print(add(3,4))

#２つの小さい方を返す
little = lambda a ,b : b if b < a else a
print(little(15,13))

#ユーロ円変換
euro_jpy = lambda euro, rate : euro * rate
print(euro_jpy(100 , 167.7))

#argで渡した数値の平均
avvrage = lambda *args : sum(args) / len(args)
print(avvrage(1,2,3,4,5,6,7))