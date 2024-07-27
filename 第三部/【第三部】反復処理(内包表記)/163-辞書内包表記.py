cure_name_en = ["cure black", "cure white", "cure bloom", "cure egret", "ltd_exp dream nichirin"]
cure_name_ja = ["キュアブラック", "キュアホワイト", "キュアブルーム", "キュアイーグレット", "特急ドリームにちりん"]

cure_dict = dict(zip(cure_name_en, cure_name_ja))
print(cure_dict)
#内包表記
cure_dict2 = {e : j for e, j in zip(cure_name_en, cure_name_ja) }
print(cure_dict2)


sample_dict = {"shimanto":1, "nanpu":2, "siokaze":3, "ishizuchi":4}
fil_dict = {
    l: r for l, r in sample_dict.items()
    if r % 2 == 0
}
print(fil_dict)


num_list = list(range(1, 11))
#内包表記なし
num_dict1 = {}
for num in num_list:
    if num % 2 == 0:
        num_dict1[num] = "even"
    else:
        num_dict1[num] = "odd"
print(num_dict1)
#内包表記あり
num_dict2 = {
    num: ("even" if num % 2 == 0 else "odd")
    for num in num_list
}
print(num_dict2)

#辞書からの内包表記
data = [
    {"name":"jiro", "age":33 ,"city": "tokyo"},
    {"name":"kyoko", "age":29, "city": "tachikawa"},
    {"name":"tansaburo", "age":25, "city":"shibuya"},
]
data_dict = {}
for d in data:
    # data_dict[d["name"]] = {"age": d["age"]}
    loop_dict = {}
    for k, v in d.items():
        print(k, v) #keyとvalueが出力される
        if k != "name":
            # data_dict[d["name"]] = {k, v}
            loop_dict[k] = v
    data_dict[d["name"]] = loop_dict
print(data_dict)

data_dict2 = {
    d["name"]: {k: v for k, v in d.items() if k != "name"} for d in data
}
        
print(data_dict2)