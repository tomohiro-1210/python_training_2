def bill(unit_price, quantity, has_app):
    amount = unit_price * quantity
    point = amount * 0.01 if has_app else 0
    return unit_price * quantity, point

my_amount, my_point = bill(unit_price=100, 10, True) #キーワード引数の後に位置引数を設定できない
my_amount, my_point = bill(100, 10, True)
print(my_amount, my_point)
