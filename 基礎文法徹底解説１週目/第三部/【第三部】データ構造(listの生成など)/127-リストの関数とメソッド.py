# +を使ってリストにdataを追加する
ltd = ["サンダーバード", "しらさぎ", "はくたか"]
pl_ltd = ltd+["北越"]
print(pl_ltd)

pl_ltd += ["加越"]
print(pl_ltd)

#extendでリストを拡張する
li_1 = [1,2,3,4]
li_2 = [5,6,7,8]
li_1.extend(li_2)
print(li_1)

# insertで要素を挿入する
num_lst = [1,2,3,4]
num_lst.insert(2, 2.5)
print(num_lst)

# popで値を取り出す
numpop = num_lst.pop(3)
print(numpop)
print(num_lst)