#アンパックとはイテラブルから
numbers = (1 ,2, 3)
a, b, c = numbers
print(a ,b ,c)

train = {
    "name": "やくも",
    "series":381,
    "speed":120
}

print(*train)
print(*train.values())
print(*train.items())