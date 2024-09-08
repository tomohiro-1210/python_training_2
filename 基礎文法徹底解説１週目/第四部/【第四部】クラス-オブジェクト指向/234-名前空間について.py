import builtins
from pprint import pprint

#グローバル変数
a = 1

def outer():
    # エンクロージング変数
    a = 2

    def inner():
        # ローカル変数
        a = 3
        print(a)

    print(a)
    inner()

print(a)
outer()
