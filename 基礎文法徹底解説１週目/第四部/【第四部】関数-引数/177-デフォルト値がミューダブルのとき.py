#ミューダブル（変更可能オブジェクト）
def greeting(name , name_list=[]):
    name_list.append(name)
    return name_list

array = greeting('いかずきん', ['だいおうイカ', 'ダゴン', 'プチアーノン', 'オセアーノン'])
print(array)

array2 = greeting('やまたのおろち')
print(array2)

array2 = greeting('キングヒドラ')
print(array2)

#ミューダブルにすると値を引き継ぐ
array2 = greeting('ヒドラ', array2)
print(array2)

array3 = greeting(array, array2)
print(array3)
print(array3[3])