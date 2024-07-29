def can_drink_alcohol(age: int):
    """
    引数 age を受け取り、20以上なら '飲酒可能です' という文字列を返す関数を実装してください。
    ただし、age の値に応じて以下の例外を発生させてください。

    age がfloat型の場合は TypeError を発生させてください。 エラーメッセージは '整数を入力してください' とします。
    age がint型以外の場合は TypeError を発生させてください。エラーメッセージは '整数以外は判定できません' とします。
    age が負の数の場合は ValueError を発生させてください。エラーメッセージは '正の数を入力してください' とします。
    age が20未満の場合は ValueError を発生させてください。エラーメッセージは'飲酒不可です' とします。
    なお、age がint型か判定するには isinstance(age, int)、float型か判定するには instance(age, float) を使います。
    """
    try:
        if age >= 20:
            return '飲酒可能' 
    except TypeError as e:
        print(e)


print(can_drink_alcohol(''))
