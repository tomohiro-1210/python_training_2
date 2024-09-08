def is_key_in_dict(target_dict, target_key):
    """
    与えられた辞書に指定したキーが含まれているか返す関数を作成してください。

    指定したキーが含まれている場合は '含まれています' を返し、含まれていない場合は '含まれていません' を返してください。
    """
    if target_dict[target_key] == target_key:
        print('含まれています')
    else:
        print('含まれていません')

#修正コード
def is_key_in_dict(target_dict, target_key):
    """
    与えられた辞書に指定したキーが含まれているか返す関数。

    指定したキーが含まれている場合は '含まれています' を返し、含まれていない場合は '含まれていません' を返します。

    Args:
        target_dict (dict): チェックする対象の辞書。
        target_key: チェックする対象のキー。

    Returns:
        str: キーが含まれているかどうかのメッセージ。
    """
    if target_key in target_dict:
        return '含まれています'
    else:
        return '含まれていません'