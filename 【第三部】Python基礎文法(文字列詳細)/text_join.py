# 文字列を結合させる様々な方法
print('java' 'script' 'JAVA')

print('Short'
      'Movie')

p = '485系かもめ'
q = '485系ハウステンボス_%s' % p # %sでstr型、文字列を結合
print(q)

number1 = 200
number2 = "clean_%d" % number1 # %dで整数を結合する。
print(number2)