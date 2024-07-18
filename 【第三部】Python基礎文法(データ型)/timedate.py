#日付時刻を表すdatetime
import datetime

# 日付時刻の表示
now = datetime.datetime.now()
print(now)

# 2020/12/25のクリスマス 
xmas = datetime.datetime(2020,12,25)
print(xmas)

#今日の日付表示
today = datetime.date.today()
print(today)

# 指定した日付
future = datetime.date(2025,2,25)
print(future)

# 時間表示
time = datetime.time(12, 12, 0)
print(time)