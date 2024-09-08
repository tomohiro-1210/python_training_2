def double_an_odd_number(int_list):
    """
    与えられた整数のリストの要素のうち、奇数だけを2倍にして、その合計を返す関数を作成してください。
    奇数は合計に含めません。
    """
    num = 0
    for i in int_list:
        if i % 2 != 0:
            num += i * 2
            print(num)
    return num

print(double_an_odd_number(int_list=[1,2,3,4,5,6,7,8,9]))