"""
Q9. お買い物付与ポイント判定プログラムプログラムを作成してください。
    (Amazon とか 楽天 での買い物をイメージ)

    お買い物金額が10,000円以上の場合は、ポイントを付与します。
    付与されるポイントは、お買い物金額の1%です。
    ただし、アプリから購入した金額に対してはポイントが2倍になります。
    また、提携クレジットカードを所持している場合は、ポイントが3倍になります。
    なお、ポイントは小数点以下を切り捨ててください。
    ※ 合計金額が10,000円に達しない場合は、ポイントは一切付与されません。

    例1) ブラウザでのお買い物金額が 10,000円の場合は、
    10,000円 × 1% = 100ポイント となります。

    例2) 10,000円のうちアプリからの購入金額が5,000円の場合は、
    5,000円 × 2% + 5,000円 × 1% = 150ポイント となります。

    例3) アプリで5,000円、ブラウザで5,000円、提携クレジットカードを所持している場合は、
    5,000円 x 1% + 5,000円 x 2% + 10,000 x 1% = 250ポイント となります。
"""
import math

browser_price = input("ブラウザからの購入金額を入力してください: ")
appli_price = input("アプリからの購入金額を入力してください: ")
has_credit_card = input("提携クレジットカードを所持していますか？(y/n): ")  # y でTrue, n でFalse

browser_price = int(browser_price)
appli_price = int(appli_price)

total_price = browser_price + appli_price

if total_price < 10000:
    print('ポイントは付与されません')
elif total_price >= 10000:
    if has_credit_card == 'y':
        borwser_point = browser_price * 0.01 
        appli_point = appli_price * 0.02
        card_point = total_price * 0.01
        borwser_point = math.floor(borwser_point)
        appli_point = math.floor(appli_point)
        card_point = math.floor(card_point)
        print('ブラウザで獲得したポイント：' + str(borwser_point))
        print('アプリで購入したポイント：' + str(appli_point))
        print('カードで購入したポイント：' + str(card_point))
    elif has_credit_card == 'n':
        borwser_point = browser_price * 0.01 
        appli_point = appli_price * 0.02
        borwser_point = math.floor(borwser_point)
        appli_point = math.floor(appli_point)
        print('ブラウザで獲得したポイント：' + str(borwser_point))
        print('アプリで購入したポイント：' + str(appli_point))
    



