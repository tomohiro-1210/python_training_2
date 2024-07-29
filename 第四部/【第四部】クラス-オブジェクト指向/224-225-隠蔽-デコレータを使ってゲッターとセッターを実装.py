class Customer:
    def __init__(self, name , age , height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    #年齢のバリテーション
    @property
    def age(self):
        return self._age # ゲッター内では _ をつける
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("年齢は半角英数字かつ整数で入力してください")
        elif value < 18:
            raise ValueError("未成年は登録できません")
        self._age = value # セッター内でも _ をつける

    #身長のバリテーション
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('身長は整数の値で入れてください')
        elif value < 0:
            raise ValueError('身長は正の値を入力してください')
        self._height = value

    #体重のエラー
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('体重は整数の値で入力してください')
        elif value < 0:
            raise ValueError("体重は正の値を入力してください")
        self._weight = value

    @property
    def bmi(self):
        return self.weight / (self.height / 100) ** 2

yamada = Customer(name="やまだじろう", age=25, height=165, weight=85)
print(yamada.age , yamada.height)
print(yamada.bmi)