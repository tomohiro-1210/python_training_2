#inputはユーザーからのデータの入力を受け付ける関数
name = input("あなたの名前を入力してください")
print("Hello", name)

ltd_exp = input("あなたの好きな特急列車を教えてください")
print(ltd_exp)

num = input("高校受験番号は何番ですか？") #普段はstrで受け取る
num = int(num) #str->intに変換して数字に対応
print(num + 3)