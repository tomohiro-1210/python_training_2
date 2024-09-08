def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(f"pos1:{pos1}")
    print(f"pos2:{pos2}")
    print(f"pos_or_kwd:{pos_or_kwd}")
    print(f"kwd1:{kwd1}")
    print(f"kwd2:{kwd2}")

f(1, 2, 3 ,kwd1=4, kwd2=5)
f(1, 2, pos_or_kwd=100 ,kwd1=4, kwd2=5)