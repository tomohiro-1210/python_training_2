# クラス：プロパティーとメソッドをひとまとめにして整理整頓をするための技術
#　クラス設計が必要になる可能性があるなと思う。

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'こんにちは。私は{self.name}です。\n年齢は{self.age}歳です。')

yamada = Human(name='ise', age=100)
yamada.say_hello()

kyoto = Human(name='masaji', age=22)
kyoto.say_hello()