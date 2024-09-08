# zlibモジュールのインポート
import zlib

def compress(path):
        
    # バイナリモードでファイルを開く（encoding引数は不要）
    with open("text.txt", "rb") as f:
        data = f.read()
        print("圧縮前のデータ", data)

    # データを圧縮する
    compressed_data = zlib.compress(data)
    print("圧縮後のデータ", data)

    # 解凍前後を比較する
    print(len(compressed_data))
    print(len(data))
    return compressed_data

comp = compress("text.txt")