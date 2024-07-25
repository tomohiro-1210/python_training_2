#タプル
tuple_num = tuple(range(10))
print(tuple_num)
tuple_len = len(tuple_num)

for num in tuple_num:
    print(num)

num_list = [1,2,3,4,5,6,7,8,9,10]
print(num_list)
num_list = tuple(num_list)
print(num_list)

#リストは可変的なデータの格納
#タプルは固定的なデータの格納

def foo(num):
    return num + 1, num ** 2

f, f2 = foo(10)
print(f, f2)

#関数の（）には変数なども入れられる
def train(name):
    return name, name*2

izumo = train('yakumo')
print(izumo)
