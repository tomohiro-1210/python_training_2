class NgativeValueError(ValueError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.__class__.__name__}: 負の値が入力されました: {self.value}"
    
class Customer:
    def __init__(self, name, age):
        self.name = name
        self._age = self._set_age(age)

    @property
    def age(self):
        return self.age
    
    @staticmethod
    def _set_age(age):
        if age < 0:
            raise NgativeValueError(age)
        return age
    
try:
    mimic = Customer("ミミック", -33)
except NgativeValueError as e:
    print(e)
else:
    print(mimic.age)