numbers = list(range(1, 11))

# 偶数要素だけを二乗
print(numbers)

squared_even_numbers = [
    x**2 for x in numbers if x % 2 == 0
]
even_dict ={ 
    y : y ** 2 for y in numbers if y % 2 == 0
}

print(squared_even_numbers)
print(even_dict)