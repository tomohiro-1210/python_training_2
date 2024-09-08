ltd_exp = {
        "kyushu":{'fukuoka':'かいおう', 'saga':'みどり', 'nagasaki':'かもめ', 'kumamoto': '有明', 'kagoshima':'きりしま', 'ooita':'にちりん', 'miyazaki': 'ひゅうが'},
        "shikoku":{'kochi': 'あしずり', 'ehime': '宇和海', 'tokushima': 'うずしお', 'kagawa': 'マリンライナー'}
    }
print(ltd_exp)
kyushu = ltd_exp["kyushu"]
shikoku = ltd_exp["shikoku"]

print(kyushu)
fukuoka = kyushu["fukuoka"]
print(fukuoka)

for k_p, k_l in kyushu.items():
    print([k_p, k_l])

for s_p, s_l in shikoku.items():
    print([s_p, s_l])

#リストの中に辞書
ltd_exp = [
    {"name": "にちりん", "series":485},
    {"name": "ひゅうが", "series":787},
    {"name": "ソニック", "series":883},
    {"name": "みどり", "series":885},
    {"name": "ハウステンボス", "series":783},
]

print(ltd_exp[0])

ltd_len = len(ltd_exp)
ltd_range = range(ltd_len)

for _ in ltd_range:
    print(_)
    print(ltd_exp[_])

for name in ltd_exp:
    print(name["name"], name["series"])