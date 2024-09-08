# 数学モジュール
import math
sqrt = math.sqrt(4900)
print(sqrt)

#サインコサインタンジェント
sin = math.sin(60)
print(sin)
cos = math.cos(60)
print(cos)
tan = math.tan(60)
print(tan)

#カレンダー
import calendar

# カレンダーの表示calender.calenderの()内は年を入れる
print(calendar.calendar(2030))

#指定した年月のカレンダーを表示 calendar.prmonth(年, 月)
print(calendar.prmonth(2024, 12))

# osモジュール
import os

current_dir = os.getcwd()
print(current_dir)

# os.mkdirで新しいディレクトリが作られる