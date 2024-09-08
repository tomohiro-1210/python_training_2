numbers = list(range(1, 20))

squared_odd_numbers_dict = {
    num: num ** 2
    for num in numbers if num % 2 == 1
}

print(squared_odd_numbers_dict)
