# import mymodule
# importはモジュール全体
# import mymodule as mm
# asはインポートしたフォルダ名を省略できる
from mymodule import Container, add, list
# from ファイル名 import クラス名で個別のクラスや関数を呼び出せる

add_result = add(1, 10)
print(add_result)

list = list()
print(list)

module_list = Container.ContainerBlock1()
print(module_list)