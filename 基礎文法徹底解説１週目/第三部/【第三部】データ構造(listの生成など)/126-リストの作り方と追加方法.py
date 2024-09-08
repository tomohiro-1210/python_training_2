list_1 = ["ミミック",]
list_1.append('追加データ')
list_1.append('ひとくいばこ')
list_1.append('フリーレン')
print(list_1)
print(list_1[2])

even_list = []
for number in range(1, 101):
    if number % 2 == 0:
        even_list.append(number)

print(even_list)

# ,で区切られたものをlistに変換
languages = 'html,css,scss,javascript,php'
lang_list = languages.split(',')
print(lang_list)
for lang in lang_list:
    print(lang)

# 文字列をリストに変換
st = 'party'
string_list = list(st)
print(string_list)

# rangeで数字を生成してリスト化
r = range(10)
print(list(r))

for _ in range(10):
    print(_)