def get＿operation(operator):
    def add(x, y):
        return x + y

    def subtract(x , y):
        return x - y

    def division(x , y):
        return x * y

    def miltiply(x , y):
        return x / y
    
    if operator == "+":
        return add
    elif operator == '-':
        return subtract
    elif operator == '*':
        return division
    elif operator == '/':
        return miltiply
    else:
        None
    
operation = get_operation('a')
result = operation(200 , 100)
print(result)