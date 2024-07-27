set_1 = {1,2,3,2,3,2,1,2,3,2,1,1}
print(set_1)
print(type(set_1))

#addで要素追加
set_1.add(4)
print(set_1)

#removeで要素削除
set_1.remove(3)
print(set_1)

#inで要素の有り無し判定
print(3 in set_1)



a = {"toba", "ise", "matsusaka"}
b = {"tsu", "suzuka", "kuwana", "ise"}


#和集合
print(a | b)
print(a.union(b))

#積集合
print(a & b)
print(a.intersection(b))

#差集合
print(a - b)
print(b - a)
print(a.difference(b))
print(b.difference(a))

#対称差
print(a.symmetric_difference(b))