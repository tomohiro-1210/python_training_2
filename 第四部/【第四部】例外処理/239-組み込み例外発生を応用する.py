def get_number(message, min_value):
    while True:
        try:
            num = int(input(message))
            if num < min_value:
                raise ValueError(f"{min_value}以上の値を入力してください")
        except ValueError:
            print('数字を入力してください')
        except KeyboardInterrupt:
            print('入力がキャンセルされました')
            break
        except AssertionError as e:
            print(e)
        else:
            return num
        
height = get_number("身長を入力してください\n" ,120)
weight = get_number("体重を入力してください\n" ,50)

bmi = weight / (height / 100) ** 2
print(bmi)

