# 親クラス
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"こんにちは{self.name}です。\n年齢は{self.age}です")

    
#子クラス
class Customer(Human):
    def __init__(self, name, age, address, school):
        super().__init__(name, age)
        self.address = address
        self.school = school

    def status(self):
        print(f'私の住んでいる場所は{self.address}。\n通っている学校は{self.school}学園です！')

saki = Customer(name="saki", age=16, address="tokyo", school="Hatsuboshi")
saki.greeting()
saki.status()
print(dir(saki))