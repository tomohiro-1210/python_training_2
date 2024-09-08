def greet(name, name_list=None):
    if name_list is None:
        name_list=[]
    print(name_list)
    name_list.append(name)
    return name_list

names = greet('John', ['Jane', 'Joe', 'Jack'])
print(names)

names = greet('delichan')
print(names)

names = greet('bob')
print(names) # ２回目の実行の時の初期値入るようになっている。

names = greet('kim')
print(names) # 前回のbobが追加されている