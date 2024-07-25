#count
fruits = ['apple', 'banana', 'orange']
banana_count = fruits.count('banana')
print(banana_count)

#reverse
fruits.reverse()
print(fruits)

#sort
ishikawa = ['suzu', 'wajima', 'anamizu', 'nanao', 'hakui', 'kahoku', 'tsubata', 'kanazawa', 'matto', 'mikawa', 'komatsu', 'kaga', 'hakusan']
ishikawa.sort()
print(ishikawa)

ishikawa_2 = ishikawa.copy()
ishikawa_2.sort(key=len)
print(ishikawa_2)