import random
have_coin = random.randint(10, 240)
def vending_machine(coin, drink_name):
    # 自動販売機関数
    if coin < 120:
        return 'コインが足りません', coin
    
    lottery_result = random.randint(1, 5)
    if lottery_result == 5:
        lottery = 'あたり'
    else:
        lottery = 'はずれ'
    
    return drink_name, coin - 120, lottery

result = vending_machine(have_coin, 'コーラ')
print(result)

