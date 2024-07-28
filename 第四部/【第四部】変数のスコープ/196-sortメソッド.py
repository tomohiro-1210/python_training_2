#sort:素のイテラブルを並び替える「破壊的メソッド」
def by_length(word):
    return len(word)

trains = ['asama', 'hakusan', 'myoko', 'minori', 'shirayuki']
trains.sort(key=by_length, reverse=True)
train_list = sorted(trains)
print(trains)
print(train_list)

def by_absolute_value(num):
    return abs(num)

nums = [1, 2, -3, 4, 5, -6, 7]
nums.sort()
print(nums)
nums.sort(key=by_absolute_value)
print(nums)