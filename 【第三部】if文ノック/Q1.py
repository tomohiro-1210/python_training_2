"""
Q1. 降水確率によって持ち物を変えるプログラムを作成してください。
    降水確率が 50% 以上の場合は「カッパ」を、
    30% 以上 50% 未満の場合は「折りたたみ傘」を、
    30% 未満の場合は「傘を持たない」を表示してください。
"""

rainy_percent = 60  # 降水確率
if rainy_percent < 30:
    print('傘を持たない')
elif 30 <= rainy_percent < 50:
    print('折り畳み傘')
elif 50 <= rainy_percent:
    print('カッパ')
