#辞書
fruits = {
    "apple": "りんご",
    "belly":"ベリー",
    "pine":"パイナップル"
          }
print(fruits["apple"])

#dictで辞書に変換
ltd_exp = dict(kochi="あしずり", ehime="宇和海", tokushima="うずしお", kagawa="マリンライナー")
print(ltd_exp)
print(ltd_exp["kochi"])
if(ltd_exp["kochi"] == "しまんと"):
    print("合致していない")