def count_up_to(max):
    count = 0
    while count < max:
        yield count
        count += 1

my_generator = count_up_to(5)
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))