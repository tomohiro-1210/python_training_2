def judge_grade(math, english, science):
    """
    成績(math, english, science)が与えられたとき、以下の条件に基づいて、成績評価を返す関数を作成してください。

    - 合計点が250点以上の場合は、'優秀です' を返す
    - 合計点が200点以上の場合は、'良いです' を返す
    - 合計点が150点以上の場合は、'可もなく不可もなく' を返す
    - 合計点が130点以上の場合は、'改善が必要です' を返す
    - 合計点が130点未満の場合は、'不合格です' を返す
    - ※ ただし、3教科のうち、どれか1つでも40点未満の場合は、'不合格です' を返す
    """
    total = math + english + science
    if math < 40 or english < 40 or science < 40:
        return '不合格です'
    else:
        if total >= 250:
            return '優秀です'
        elif total >= 200:
            return '良いです'
        elif total >= 150:
            return '可もなく不可もなく'
        elif total >= 130:
            return '改善が必要です'
        else:
            return '不合格です'

print(judge_grade(65, 50, 85))