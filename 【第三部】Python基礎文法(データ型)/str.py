# str型はシングルクォートやダブルクォートで良い
print("ダブルクォートで囲む")
print('シングルクォートで囲む')

# ダブルクォートでシングルクォートを使用する例
print("I'm mimic.")
print("私は'勇者'である")

# シングルクォートをダブルクォートで使用する例
print('"魔法使い"はドラクエの職業の一つでもあるが、プリキュアでも出てくる')

# age = input("年齢は？")
# height = input("身長は？")

# print(type(age), type(height))
# print(int(age) + 10)

#特殊文字
v_bool = bool(100)
print(v_bool)

# \で特殊文字扱いにする
print('I\'m Erika')
print("I'm \"Tsubomi\"")
print("I'm \\nPandoraBox") #\nを文字列として扱いたい場合

#改行をする場合
print("今日は朝から晴れています。\n9時から診療所に行って健康診断。\n2時過ぎには心療内科に行ってまどころ先生との定期診察。\n20時30分からはオンラインでうえの先生とのカウンセリング。\n病院豪華3本立てですねぇ・・・（笑）\n今日の健康診断担当医は誰でしょうか？\nまさかのしんの先生かなぁ？？")

age = 40
print("I'm " + str(age) + " years old.")