"""
Q2. 年収が扶養範囲内か判定するプログラムを作成してください。
    年収が1,030,000円以下の場合は「扶養範囲内です」と表示し、
    1,030,000円より大きい場合は「扶養範囲外です」と表示してください。
"""

income = int(input("年収を入力してください。:"))


if income <= 1030000:
    print("扶養範囲内です")
else:
    print("扶養範囲外です")
