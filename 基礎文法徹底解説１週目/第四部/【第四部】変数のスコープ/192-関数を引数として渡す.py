def add(x, y):
    return x + y

def subtract(x , y):
    return x - y

def division(x , y):
    return x * y

def miltiply(x , y):
    return x / y

def calcrate(func, x , y):
    return func(x, y)

add_a = add(1, 2)
print(add_a)

result_d = calcrate(division, 100 ,20)
print(result_d)

result_s = calcrate(subtract, 100 ,20)
print(result_s)

result_m = calcrate(miltiply, 100 ,20)
print(result_m)




def add2(*args , func):
    return func(*args)

add_v2 = add2([1,2,3,4,5] , func=sum)
print(add_v2)