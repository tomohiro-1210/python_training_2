def square(x):
    return x * x

def add_10(x):
    return x + 10

nums = [1, 2, 3, 4, 5]
squares = map(add_10, nums)

for number in squares:
    print(number)


#小文字のリストを大文字のリストに変換する
def to_upper(s):
    return s.upper()

langs = ['English', 'French', 'Spanish', 'Chinese', 'Japanese']
uppers = map(to_upper, langs)
print(list(uppers))

def to_shaku(meter):
    return meter * 0.302

meters = [100, 150, 200]
shakus = map(to_shaku, meters)

for meter ,shaku in zip(meters, shakus):
    print(f'{meter} m = {shaku} shaku')