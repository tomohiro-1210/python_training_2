def plus(a, b, c):
    return a + b + c

def minus(a ,b, c):
    return a - b - c

def multiply(a ,b, c):
    return a * b * c

def division(a ,b, c):
    return a / b / c

def calculate(func, a ,b, c):
    return func(a, b ,c)

def return_calc(calc_name):
    if calc_name == "plus":
        return plus
    elif calc_name == "minus":
        return minus
    elif calc_name == "multiply":
        return multiply
    elif calc_name == "division":
        return division
    
result_plus = calculate(return_calc("plus") ,100 , 20 , 5)
result_minus = calculate(return_calc("minus") ,100 , 20 , 5)
result_multiply = calculate(return_calc("multiply") ,100 , 20 , 5)
result_division = calculate(return_calc("division") ,100 , 20 , 5)
print(result_plus)
print(result_minus)
print(result_multiply)
print(result_division)