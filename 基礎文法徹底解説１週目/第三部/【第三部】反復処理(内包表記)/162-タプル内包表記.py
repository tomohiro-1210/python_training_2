my_tuple = tuple(x for x in range(10))
print(my_tuple)

even_tuple = []
for _ in range(101):
    if _ % 2 == 1:
        even_tuple.append(_)
print(even_tuple)