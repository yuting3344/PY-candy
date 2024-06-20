# 編號：CANDY-015
# 程式語言：Python
# 題目：把原本的字串拆解成 2 個字元一組，若不足 2 個字則補上底線
# 範例：
#      "abcdef" -> ['ab', 'cd', 'ef']
#      "abcdefg" -> ['ab', 'cd', 'ef', 'g_']


def pairs_string(input_str):
    pairs = [
        input_str[i : i + 2] if i + 1 < len(input_str) else input_str[i] + "_"
        for i in range(0, len(input_str), 2)
    ]
    return pairs


print(pairs_string("abcdef"))
# ["ab", "cd", "ef"]
print(pairs_string("abcdefg"))
# ["ab", "cd", "ef", "g_"]
print(pairs_string(""))
# []
