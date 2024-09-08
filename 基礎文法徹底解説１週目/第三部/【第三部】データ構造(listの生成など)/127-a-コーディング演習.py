static_langs = ['C', 'C++', 'Java', 'C#']
dynamic_langs = ['Python', 'JavaScript', 'PHP', 'Ruby']

# append メソッドを使って以下の構造、データのリストを新たに作成、表示してください。
# [['C', 'C++', 'Java', 'C#'], ['Python', 'JavaScript', 'PHP', 'Ruby']]
nested_langs = [static_langs]
nested_langs.append(dynamic_langs)
print(nested_langs)

# extend メソッドを使って以下の構造、データのリストを新たに作成、表示してください。
# ['C', 'C++', 'Java', 'C#', 'Python', 'JavaScript', 'PHP', 'Ruby']
extended_langs = static_langs.copy()
extended_langs.extend(dynamic_langs)
print(extended_langs)  # ['C', 'C++', 'Java', 'C#', 'Python', 'JavaScript', 'PHP', 'Ruby']

# pop メソッドを使って nested_langs から 要素 'Python' を取り出し変数に格納、出力してください。
dynamic_langs_py = nested_langs[1]
python = dynamic_langs_py.pop(dynamic_langs_py.index('Python'))
print(python)

# insert メソッドを使って extended_langs の 'Java' の後に 'Swift' を追加、表示してください。
java_index = extended_langs.index('Java')
extended_langs.insert(java_index + 1, 'Swift')
print(extended_langs)  # ['C', 'C++', 'Java', 'Swift', 'C#', 'Python', 'JavaScript', 'PHP', 'Ruby']
