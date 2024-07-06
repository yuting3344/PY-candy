# 編號：CANDY-020
# 程式語言：JavaScript
# 題目：檢查字串的 x 跟 o 的數量是不是一樣多，不分大小寫


import re


def xx_oo(words):
    all_lower = words.lower()
    filter_char = re.sub("[^oxX]", "", all_lower)
    count_o = filter_char.count("o")
    count_x = filter_char.count("x")
    return count_o == count_x


print(xx_oo("ooxx"))
# true
print(xx_oo("xxoo"))
# true
print(xx_oo("xxooo"))
# false
print(xx_oo("xoox"))
# true
print(xx_oo("ooAA"))
# false
print(xx_oo("xoXoA"))
# true
