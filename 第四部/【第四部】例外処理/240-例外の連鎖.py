def sum_numbers(num_list):
    try:
        return sum(num_list)
    except TypeError as e:
        print('sum_numbers', e)
        raise ValueError('リストに数値以外の要素が含まれています') from e
    
nums = [1, 2, 'Three']
# nums = [1, 2, 3]
try:
    print(sum_numbers(nums))
except ValueError as e:
    print(e)
    print(e.__cause__)
