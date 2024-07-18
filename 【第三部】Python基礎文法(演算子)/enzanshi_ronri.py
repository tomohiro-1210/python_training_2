# or:どちらかが合致したらTrueになる
result = True or False
print(result)

#変数に入れる例
a = 1 == 2
b = 221 == 221
result_1 = a or b
print(result_1)

list_a = [1,2,3]
list_b = [1,2,3]
result_2 = list_a == list_b
result_3 = list_a == list_b
result_4 = result_2 or result_3 #orはどちらかが合致したとき
result_5 = result_2 and result_3 #andは両方が合致したとき
print(result_4)
print(result_5)