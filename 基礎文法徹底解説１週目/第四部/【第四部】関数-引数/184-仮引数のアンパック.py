def sum_func(*args):
    print(args * 2)
    total = sum(args * 2)
    return total

nums = [1, 2, 3, 4 ,5]
multi = sum_func(*nums)
print(multi)

#メニューと価格の表示
def print_menu(**kwargs):
    for dish, price in kwargs.items():
        print(f'{dish} :{price}円')

print_menu(katsumeshi=900, tamagoyaki=700, gosasoro=90)