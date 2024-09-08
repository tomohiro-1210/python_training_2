"""
Q3. 消費税率を判定し、税込み価格(整数)を表示するプログラムを作成してください。
    消費税率は10%、ただし食料品かつ持ち帰りの場合は8%です。

    食料品かどうかはis_foodで判定します。(0で食料品以外、1で食料品)
    持ち帰りかどうかはis_takeoutで判定します。(0で店内飲食、1で持ち帰り)
    また、is_foodが0と1以外の場合、「不正な値です」と表示してください。
    また、is_takeoutが0と1以外の場合、「不正な値です」と表示してください。
    さらに、変数 is_takeout は適切な位置に再配置してください。

    また、プログラムを強制終了させるときは、exit()を使用してください。
    また、「何もしない」を表現するには pass 文が使えます。
"""

amount = int(input('お買上金額を入力してください。:'))  # お買上金額
tax_rate = 0.1  # 消費税率
is_food = input('以下の数値を入力してください。\n0) 食料品以外\n1) 食料品\n:')

if is_food == '0':
    pass
elif is_food == '1':
    is_takeout = input('以下の数値を入力してください。\n0) 店内飲食\n1) 持ち帰り\n:')
    if is_takeout == '0':
        pass
    elif is_takeout == '1':
        tax_rate = 0.08
    else:
        print('不正な値です')
        exit()
else:
    print('不正な値です')
    exit()

total_amount = int(amount * (1 + tax_rate))
print(total_amount)
