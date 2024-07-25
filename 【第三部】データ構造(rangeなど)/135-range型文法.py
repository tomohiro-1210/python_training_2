# range
for _ in range(11):
    print(str(_))

num_2 = range(10, 100, 2)
print(list(num_2))

for num in num_2:
    if num <= 50:
        print(num)
    else:
        print('50以上')

