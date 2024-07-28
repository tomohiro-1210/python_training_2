def is_even(x):
    return x % 2 == 0

nums = list(range(1, 51))

even_nums = filter(is_even, nums)
print(even_nums)
# print(list(even_nums))

for even_num in even_nums:
    print(even_num)

#Aの文字判定
def start_widh_A(word):
    return word.startswith('A')

words = ['Akagi', 'Kusatsu', 'Banana', 'Apple', 'Lemon']
start_a = filter(start_widh_A, words)
for word in start_a:
    print(word)