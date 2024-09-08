# 親クラス(継承元)
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"こんにちは{self.name}です。\n年齢は{self.age}です")

    
#phpなら　class Customer extends Humanとかくはず
#子クラス(継承先)
class Customer(Human):
    # def __init__(self, name, age, address, school):
    #     super().__init__(name, age)
    
    #*継承元の変数を*argsに変えても問題ない
    def __init__(self, *args, address, school):
        super().__init__(*args)
        self.address = address
        self.school = school

    #こいつがオーバーライドか。
    def status(self):
        print(f'私の住んでいる場所は{self.address}。\n通っている学校は{self.school}学園です！')

# saki = Customer(name="花海咲季", age=16, address="愛知県", school="初星")
# *argsを使う場合は継承元の変数は省略
saki = Customer("花海咲季", 16, address="愛知県", school="初星")
saki.greeting()
saki.status()
# print(dir(saki))

# chisato = Customer(name="嵐ちさと", age=18, address="原宿", school="結ヶ丘")
# *argsを使う場合は継承元の変数は省略
chisato = Customer("嵐ちさと", 18, address="原宿", school="結ヶ丘")
chisato.greeting()
chisato.status()

