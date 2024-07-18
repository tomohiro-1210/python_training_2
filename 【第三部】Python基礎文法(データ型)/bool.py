# boolは真偽を表す型
age = 21
adult = age >= 20
print(bool(adult))

train_speed = 100
branch_speed = train_speed <= 60
if branch_speed:
    print("信号は黄色、制限速度60以下")
else:
    print("信号は青、制限解除。本線進行！") 