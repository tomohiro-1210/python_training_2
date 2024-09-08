def get_number(message="数字を入力してください"):
    while True:
        try:
            num = int(input(message))
        except ValueError:
            print('数字を入力してください')
        except KeyboardInterrupt:
            print('入力がキャンセルされました')
            break
        else:
            return num
        
height = get_number("身長を入力してください\n")
weight = get_number("体重を入力してください\n")

bmi = weight / (height / 100) ** 2
print(bmi)

