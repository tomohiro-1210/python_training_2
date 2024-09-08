"""
Q8. 以下の選択問題の正解をinput関数で入力させ、正解を判定するプログラムを作成してください。

問題
    pythonインタプリタを終了するコマンドを、選択肢の中から選びなさい。

選択肢
    1. exit()
    2. quit()
    3. close()
    4. break()
"""

choice = int(input("pythonインタプリタを終了するコマンドを、選択肢の中から選びなさい。\n\n"
                   "選択肢\n"
                   "1) exit()\n"
                   "2) quit()\n"
                   "3) close()\n"
                   "4) break()\n"
                   "数字を入力してください:"))

if 1 <= choice <= 4:
    if choice == 1:
        print("正解です。")
    else:
        print("不正解です。")
else:
    print("1から4の数字を入力してください。")
