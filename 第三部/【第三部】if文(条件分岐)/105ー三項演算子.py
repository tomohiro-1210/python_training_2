#三項演算子
x = -1
y = "ポジティブ" if x > 0 else "ネガティブ"

print(y)

#昭和か平成か
year = 1985
genelation = "昭和" if year < 1990 else "平成"
print(genelation)

#成人なのか未成年なのか
age = 18
is_adult = True if age >= 18 else False
print(is_adult)
adult_year = 2020
adult = "２０歳から成人だった時代" if adult_year <= 2021 else "１８歳から成人の時代"
print(adult)