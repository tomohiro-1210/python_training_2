#関数のdocstring
def add(a, b):
    """
    2つの数値を加算する関数。

    Args:
        a (int or float): 1つ目の数値。
        b (int or float): 2つ目の数値。

    Returns:
        int or float: 2つの数値の合計。
    """
    return a + b

#クラスのdocstring
class Animal:
    """
    動物クラス。

    Attributes:
        name (str): 動物の名前。
        age (int): 動物の年齢。
    """

    def __init__(self, name, age):
        """
        Animalクラスのコンストラクタ。

        Args:
            name (str): 動物の名前。
            age (int): 動物の年齢。
        """
        self.name = name
        self.age = age

    def speak(self):
        """
        動物が話すメソッド。

        Returns:
            str: 動物の話す内容。
        """
        return f"{self.name} says hello!"

#モジュールのdocstring
"""
このモジュールは、基本的な算術演算を提供します。

関数:
    add(a, b): 2つの数値を加算する。
    subtract(a, b): 2つの数値を減算する。
"""

def add(a, b):
    """
    2つの数値を加算する関数。

    Args:
        a (int or float): 1つ目の数値。
        b (int or float): 2つ目の数値。

    Returns:
        int or float: 2つの数値の合計。
    """
    return a + b

def subtract(a, b):
    """
    2つの数値を減算する関数。

    Args:
        a (int or float): 1つ目の数値。
        b (int or float): 2つ目の数値。

    Returns:
        int or float: 2つの数値の差。
    """
    return a - b

