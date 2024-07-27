cure_name_en = ["cure black", "cure white", "cure bloom", "cure egret", "ltd_exp dream nichirin"]
cure_name_ja = ["キュアブラック", "キュアホワイト", "キュアブルーム", "キュアイーグレット", "特急ドリームにちりん"]

cure_dict = dict(zip(cure_name_en, cure_name_ja))
print(cure_dict)

#内包表記
cure_dict2 = {e : j for e, j in zip(cure_name_en, cure_name_ja) }
print(cure_dict2)

num_list = list(range(1, 11))
num_dict = {
    num: ("even" if num % 2 == 0 else "odd")
    for num in num_list
}
print(num_dict)

