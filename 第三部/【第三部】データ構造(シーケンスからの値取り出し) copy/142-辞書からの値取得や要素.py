
ltd_exp = dict(kochi="あしずり", ehime="宇和海", tokushima="うずしお", kagawa="マリンライナー")

#要素の追加
ltd_exp['okayama'] = "南風"
print(ltd_exp)

ltd_exp.update({"yamaguchi":"スーパーおき", "shimane":"やくも"})
print(ltd_exp)

#要素の取得
print(ltd_exp.get('okayama'))

