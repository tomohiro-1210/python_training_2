# 変数の命名規則は半角英数字とアンダーバーが推奨される
# 例⇒data_exampleとか

# _を一時的に利用する
for _ in range(100):
    print(_)

precure = "キュアブラック"
print(precure)

tax_rate = 0.1
amount = 10000 #amountは売上金額という意味か。
tax = amount * tax_rate
print(tax)

hakubi_stations = ["倉敷", "清音", "総社", "豪渓", "日和", "美袋", "備中広瀬", "備中高梁", "木野山", "備中川面", "方谷", "井倉", "石蟹", "新見"]
for hakubi in hakubi_stations:
    print(hakubi)
