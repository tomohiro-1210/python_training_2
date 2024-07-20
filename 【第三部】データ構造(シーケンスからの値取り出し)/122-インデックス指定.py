#　インデックスを指定してシーケンスから値を取り出す方法
import random

rd1 = random.randint(0 , 9)
print(rd1)

list =[0, 1 ,2, 3, 4, 5, 6, 7, 8, 9]

print(list[0])
print(list[-1])
print(list[1:7])

names = ['雷鳥' , 'しらさぎ', '加越', 'はくたか', '北越']
print(names[0])
print(names[-1])

pg = 'precure'
print(pg[-2])
print('r' == pg[-2])
print('r' == pg[2])