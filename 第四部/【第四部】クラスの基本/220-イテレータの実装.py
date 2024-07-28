class CountDown:
    def __init__(self, start):
        self.number = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        elif self.number == 5800:
            exit()
        self.number -= 1
        return self.number + 1
    
count_million = CountDown(100)
for count_num in count_million:
    print(count_num)

#残金でどのくらいのお寿司ネタを握れるか

import random 
SUSHI = [
    {"name": "たまご", "price":100},
    {"name":"納豆" , "price":150},
    {"name":"きゅうり" , "price":150},
    {"name":"まぐろ" , "price":300},
    {"name":"サーモン" , "price":250},
    {"name":"焼きサーモン" , "price":350},
    {"name":"のどぐろ" , "price":800},
]

class Itamae:
    def __init__(self, deposit):
        print(f'{deposit}円の予算内で握りましょう')
        self.deposit = deposit

    def __iter__(self):
        return self
    
    def __next__(self):
        neta_list = [neta for neta in SUSHI if neta['price'] <= self.deposit]

        if len(neta_list) == 0:
            print('お金がない・・・ネタを握ることができないようだ・・・')
            raise StopIteration
        
        neta = random.choice(neta_list)
        self.deposit -= neta["price"]
        return neta

itamae1 = Itamae(20000)
for neta in itamae1:
    print(f'{neta['name']}:{neta['price']}円あがり！\nなお残金は{itamae1.deposit}円')