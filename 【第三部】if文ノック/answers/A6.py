"""
Q6. 送料計算プログラムを作成してください。
    カート金額が6,000円以上の場合は送料無料とし、
    そうでない場合は送料として500円を加算して、
    最終的なお買上金額を表示するプログラムを作成してください。
"""

cart = int(input("カート金額を入力してください。:"))
SHIPPING = 500  # 送料
judgement = 6000

if cart >= judgement:
    print(f"お買上金額は{cart}円です。")
else:
    print(f"お買上金額は{cart + SHIPPING}円です。")
