def aaa():
    pass

text = str(aaa())
print(text * 44)

def add(x, y):
    z = x + y
    if z <= 10:
        add_result = "10以下なのでアウト"
    else:
        add_result = "10より大きいのでセーフ"
    return add_result

print(add(7, 8))
print(add(7, 0))

def error(name):
    if name == '':
        error = "名前を入力してください"
    else:
        error = name
    return error

print(error(''))
print(error('安倍晋三首相'))

#自販機に例えたサンプルコード
def vending_machine(coin):
    import random
    price = random.randint(50, 150)
    if coin < price:
        return "持ち金が足りません"
    
    lottery_result = random.randint(50, 1000)
    lottery = ''
    if lottery_result == 100:
        lottery = "あたり"
    else:
        lottery = "はずれ"
    
    return "おでん", price - coin, lottery

print(vending_machine(100))

