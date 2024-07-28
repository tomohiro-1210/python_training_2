def precure_array(*args):
    global menbers #ローカル変数をどこでも変数にする
    menbers = [] #この時点ではmenbersは空っぽ
    for menber in args:
        menbers.append(menber) #プリキュアが入っていく
    print(menbers) #プリキュアが出力される

precure_array('キュアブロッサム', 'キュアマリン', 'キュアサンシャイン', 'キュアムーンライト')
menbers = ['ゆったりやくも', 'アコモやくも', 'みどりやくも', 'スーパーやくも'] #やくもが入る
print(menbers)