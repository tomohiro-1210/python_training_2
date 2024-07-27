#シーケンスの比較
num_list1 = [1, 2, 3]
num_list2 = [1, 2, 3]
num_list3 = [4, 5, 6]

print(num_list1 == num_list2)
print(num_list1 == num_list3)
print(num_list3 >= num_list2)

num_list11 = [11, 12]
num_list12 = [11, 12, 13, 14]
num_list13 = [11, 12 ,13]

print(num_list11 >= num_list12)
print(num_list11 >= num_list13)
print(num_list11 <= num_list12)
print(num_list11 <= num_list13)
print(num_list12 >= num_list13)
print(num_list12 <= num_list13)

num_list21 = [11, 21, 31]
num_list22 = (11, 21, 31)
print(num_list21 == num_list22)
print(num_list21 == list(num_list22))
print(tuple(num_list21) == num_list22)