# 文字のエンコードとdocstring
array = '''
ミミックは
いつも宝箱に
化けており、
主人公が宝箱を開けると
時々襲い掛かってくる
ことがあります
'''
print(array)

# ドックストリング
def greet(name):
    """
    あいさつをする関数

    :param name:名前
    :return: なし
    """
    print(f"Good morning, my name is {name}")

greet("Taro")
greet("Slime")
print(greet.__doc__)

