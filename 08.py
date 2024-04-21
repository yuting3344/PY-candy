# 編號：CANDY-008
# 程式語言：Python
# 題目：傳入一字串，計算得分最高的字
#      英文字母 a 得 1 分、b 得 2 分、c 得 3 分，以此類推。
#      所有傳入的字都是小寫。


def highest_score_Word(input):
    input = input.upper()  # 轉大寫判斷unicode
    words = input.split()
    max_score = 0
    max_score_word = ""

    for word in words:
        score = sum(ord(char) - 64 for char in word if "A" <= char <= "Z")
        if score > max_score:  # 迴圈中用串列推導式判斷字母並更新
            max_score = score
            max_score_word = word

    return max_score_word.lower()


print(highest_score_Word("lorem ipsum dolor sit amet"))
# 印出 ipsum
print(highest_score_Word("heyn i need a rubygem up to build this"))
# 印出 rubygem
print(highest_score_Word("in time machine there are some bugs"))
# 印出 there
