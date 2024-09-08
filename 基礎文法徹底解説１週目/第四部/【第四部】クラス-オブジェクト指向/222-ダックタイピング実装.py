class Wonderful:
    def __init__(self, name):
        self.nane = name

    def speak(self):
        return 'いっしょにあそぼ！！'

class Nyamy:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return '仕方がない、かまってあげる💛'
    
class Rabbit:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name}'
    
iroha = Wonderful("こむぎ")
mayu = Nyamy("ゆき")
daifuku = Rabbit("大福")

print(iroha.speak(), mayu.speak() , daifuku.speak())