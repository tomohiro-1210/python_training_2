class LtdExp:
    def __init__(self, name, maxspeed):
        self.name = name
        self.maxspeed = maxspeed

    def running(self):
        return f"最高時速{self.maxspeed}km/hで、特急{self.name}が走っております"
    
class Rapid():
    def __init__(self, name, maxspeed):
        self.name = name
        self.maxspeed = maxspeed
        
    def running(self):
        return f"最高時速{self.maxspeed}km/hで、快速{self.name}が走っております"

#多重継承。最初に継承指定したクラスが指定される。
class RapidLE(LtdExp, Rapid):
    def __init__(self, *args):
        super().__init__(*args)

keikyu = RapidLE("2100形", 120)
print(keikyu.running())


        