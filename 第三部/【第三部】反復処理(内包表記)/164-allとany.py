# all():複数の要素がすべて条件を満たすか？
# any():複数の要素のうち、どれかが条件を満たすか？

list1 = [True, True, True]
list2 = [True, False, True]
list3 = [False, False, False]

print("list1,allは:" + str(all(list1)))
print("list2,allは:" + str(all(list2)))
print("list3,allは:" + str(all(list3)))

print("list1,anyは:" + str(any(list1)))
print("list2,anyは:" + str(any(list2)))
print("list3,anyは:" + str(any(list3)))

cau1 = [1 == 2, 2 == 2, 3 != 4]
print("cau1,allは:" + str(all(cau1)))
print("cau1,anyは:" + str(any(cau1)))

yakumo = 7
nanpu = 6
shiokaze = 8

okayama = [yakumo, nanpu, shiokaze]
result = all(ltd_exp_cars >= 5 for ltd_exp_cars in okayama )
if result:
    print("多客期")
else:
    print("閑散期")

#辞書とforwを使った例
programs = {
    "html": 80,
    "css": 80,
    "javascript" : 80,
    "PHP" : 70, 
    "python" : 80
}
pg_tect = all(program >= 70 for program in programs.values())
if pg_tect:
    print("採用")
else:
    print("不採用")