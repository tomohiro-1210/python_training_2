
def monster(name:str, number:int, height:float) -> str:
    return f"私の名前は{name}、モンスターナンバーは{number}、高さは{height}なのでアール"
#期待値？
name: str = "mimic"
number: int = 30
height:float = 170.00

print(monster(name, number, height))


#リストなどのアノテーション
lst: list[int] = [1, 2, 3]
dic: dict[str, int] = {'a':1 , "b":2}
print()