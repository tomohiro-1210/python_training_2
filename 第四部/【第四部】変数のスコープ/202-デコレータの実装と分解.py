# デコレーターとは：関数に機能をデコレートをするためのシンタックスシュガー
# シンタックスシュガー:プログラミング言語の構文を簡略化して書きやすくするための機能や記法

import time #時間のlibrary読み込み
def timer_decorateor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"関数{func.__name__}を実行するばい")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(F"{end_time - start_time:.2f}秒かかりました。")
        return result
    print(f"関数{func.__name__}を受け取りました")
    return wrapper

def total_function(n):
    total = 0
    for i in range(n + 1):
        total += i
        return total

total_func_decorated = timer_decorateor(total_function)
result = total_func_decorated(100000 * 1000000)
print(result)