def square(x):
    return x * x

numbers = [1 ,2, 3, 4 ,5]
squares = map(square, numbers)
# print(tuple(squares))
print(list(squares))

