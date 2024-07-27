#*argsは引数のタプル
def sum_func(*args):
    print(args)
    return sum(args)

total = sum_func(1,2,3,4,5)
print(total)

#キーワード指定
def sum_func2(multi, *args, div=100):
    print(multi, div)
    print(args)
    return sum(args)

total1 = sum_func2( 10, 1,2,3,4,5 ,div=100)
print(total1)