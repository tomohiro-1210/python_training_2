def judge_grade(grade): #gradeが仮引数
    if grade >= 90:
        return '優秀です'
    elif grade < 90 and grade >= 80:
        return '良いです'
    elif grade < 80 and grade >= 70:
        return '可もなく不可もなく'
    elif grade < 70:
        return '改善が必要です'
print(judge_grade(80)) #80が実引数
    