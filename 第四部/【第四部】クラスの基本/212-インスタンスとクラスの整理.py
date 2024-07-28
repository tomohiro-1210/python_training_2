class Human:
    population = '90億人'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'こんにちは。私は{self.name}です。\n年齢は{self.age}歳です。')

    def say_hello(self):
        print(self)


yamada = Human(name='ise', age=100)
kyoto = Human(name='masaji', age=22)
sakata = Human(name='kyougai', age=200)

Human.say_hello(yamada)