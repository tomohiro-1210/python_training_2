try:
    num = int(input("数値を入力\n"))
    result = 10 / num
    print(result)
except ValueError as e:
    print(f'数値を入力してください {e}')
except ZeroDivisionError as e:
    print(f'0で割り切れん {e}')
# except(ValueError, ZeroDivisionError, KeyboardInterrupt) as e:
#     print(f'エラーが発生しました{e}') 
else:
    print(result)
finally:
    print('処理を終了します')
