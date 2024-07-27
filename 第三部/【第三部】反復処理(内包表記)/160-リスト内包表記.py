#通常の書き方
squares = []
for _ in range(10):
    squares.append(_**2)

print(squares)

#内包表記
list_num = [x**2 for x in range(10)]
print(list_num)

list_num2 = [x**2 for x in range(50) if x % 2 == 1]
print(list_num2)

#小文字を大文字に
fruits = ["cherry", "lime", "whip", "belly", "peach", "slime"]
fruits_big = []
for fruit in fruits:
    fruits_big.append(fruit.upper())

print(fruits_big)

#内包表記
fruits2 = [fruit2.upper() for fruit2 in fruits if len(fruit2) == 5]
print(fruits2)

#指定した文字列で始まる物だけのリスト
hs = "阪神"
stations = ["阪神大阪梅田駅", "阪急大阪梅田駅", "阪神福島駅", "京阪京橋駅", "近鉄鶴橋駅", "阪神西九条駅", "京阪中之島駅", "近鉄奈良駅", "阪急桂駅", "阪神尼崎駅", "近鉄五位堂駅" ]
hanshin_stations = []

for station in stations:
    if station.startswith(hs):
        hanshin_stations.append(station)

print(hanshin_stations)

#内包表記
stations2 = [station.replace(hs, "") for station in stations if station.startswith(hs)]
print(stations2)