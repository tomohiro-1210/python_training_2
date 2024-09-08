# in演算子
text = "kyoto osaka kobe"
print('kyoto' in text)
print('tomo' in text)
print('to' in text)

# height  = 100
# print(100 in height) #int型では使えない

#コーディング演習
result_1 = 'Py' in 'python'
result_2 = 'python' in 'py'
result_3 = 'Python' in ['thon', 'python', 'py']

# 以下のprint関数の出力結果が全てTrueになるようにしてください。
print(result_1 == False )
print(result_2 == False )
print(result_3 == False )


result_4 = 'Java' in 'JavaScript'
result_5 = 'React' in 'act'
result_6 = 'Go' in ['Go', 'Python', 'JavaScript']

# 以下のprint関数の出力結果が全てTrueになるようにしてください。
print(result_4 == True )
print(result_5 == False )
print(result_6 == True )