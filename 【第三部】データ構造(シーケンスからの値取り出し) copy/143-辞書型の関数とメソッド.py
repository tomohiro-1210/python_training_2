ltd_exp = dict(kochi="あしずり", ehime="宇和海", tokushima="うずしお", kagawa="マリンライナー")
print(ltd_exp)

#要素の長さ
print('要素の長さ:' + str(len(ltd_exp)))

#削除
del ltd_exp['kagawa']
print(ltd_exp)

ltd_exp['kagawa'] = 'morning'
print(ltd_exp)

#key
for ltd_k in ltd_exp.keys():
    print(ltd_k)

#value
for ltd_v in ltd_exp.values():
    print(ltd_v)

#items
for k, v in ltd_exp.items():
    print([k, v])

#pop
print(ltd_exp.pop('kochi'))
print(ltd_exp)

ltd_exp['kochi'] = 'いごっそう'
print(ltd_exp)


#in演算子
print('kochi' in ltd_exp)
print(ltd_exp.items())
result1 = ('kagawa', 'morning') in ltd_exp.items()
result2 = ('kochi', 'あしずり') in ltd_exp.items()
print(result1)
print(result2)