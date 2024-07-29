# reモジュール
import re
# reは正規判定モジュール

pattern = re.compile(r'//[\w.-]+/?[\w.]+')

mimic = 'mimic'

# 文字列に対してパターンをマッチさせる
match = pattern.match(mimic)  # patternに対してmimicをマッチさせる

# マッチ結果の確認
if match:
    print("マッチしました！")
else:
    print("マッチしませんでした。")