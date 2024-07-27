def sample_func(*args , d , **kwargs): #kwargsの中身は辞書として渡される
    print(args)
    print(d)
    print(kwargs)
    for key_word in kwargs:
        if key_word == 'name':
            print('name is', kwargs[key_word])



sample_func(100, 200, d='ひとくいばこ', name='mimic', age=25, city='tokyo') #これの引数が辞書になる

