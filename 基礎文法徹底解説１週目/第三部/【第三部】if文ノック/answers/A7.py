"""
Q7. 七五三判定プログラムを作成してください。
    男の子の場合は5歳で「五歳男の子」と表示し、
    女の子の場合は7歳で「七歳女の子」3歳で「三歳女の子」と表示してください。
    それ以外の場合は「七五三ではありません」と表示してください。
    また、性別入力が m, f 以外の時の入力を考慮してください。

    プログラムを強制終了させるには、exit() を使います。
"""

age = input("年齢を入力してください: ")
gender = input("性別を f か m で入力してください。\nf) 女性\nm) 男性\n: ")
message = ""

if gender == "f":
    if age == "7":
        message = "七歳女の子"
    elif age == "3":
        message = "三歳女の子"
elif gender == "m":
    if age == "5":
        message = "五歳男の子"
else:
    print("不正な値です")
    exit()

if message:
    print(message)
else:
    print("七五三ではありません")
