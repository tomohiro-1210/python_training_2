# len関数
print(len('hanshin electric railway'))
length = [1 ,2, 3, 4, 5, 6, 7,8 ,9]
print(len(length))

s = 'kyoto'
print(s.strip('k'))
y = s.strip('o')
print(y)

# zfillメソッド
num = 123455321
print(str(num).zfill(10))

#findメソッドとindexメソッド
f = 'mimic mimic'
print(f.find('m', 4, 9))
print(f.index('m', 4, 9))