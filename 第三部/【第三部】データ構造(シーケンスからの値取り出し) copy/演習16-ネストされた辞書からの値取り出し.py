# my_dict を直接編集しないこと
my_dict = {
    "日本": {
        "東京": 15,
        "大阪": 16
    },
    "アメリカ": {
        "ニューヨーク": 12,
        "ロサンゼルス": 19
    }
}
# my_dict を直接編集しないこと

# 東京の温度(15)を取り出す
tokyo = my_dict["日本"]["東京"]
print(tokyo)

# ロサンゼルスの温度(19)を取り出す
los_angeles = my_dict["アメリカ"]["ロサンゼルス"]
print(los_angeles)

# 日本にkeyが福岡でvalueが20のデータを追加する
my_dict["日本"]["福岡"] = 20
print(my_dict)

# アメリカにkeyがワシントンvalueが17のデータを追加する
my_dict["アメリカ"]["ワシントン"] = 17
print(my_dict)

# 新たにkeyがインドでvalueに以下の辞書を持つデータを追加する
# keyがデリーでvalueが25、keyがムンバイでvalueが30
my_dict.update({"インド":{"デリー":25, "ムンバイ":30}})
print(my_dict)

