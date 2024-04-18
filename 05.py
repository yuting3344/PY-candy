# 編號：CANDY-005
# 程式語言：Python
# 題目：完成函數的內容，把傳進去的數字的每個位數平方之後組合在一起


def square_digits(num):
    result = ""  # 定義一個空字串

    for i in str(num):
        result += str(
            int(i) ** 2
        )  # 在 str 的迴圈中，先將字串轉 int ,平方後轉字串再推入""
    return result


print(square_digits(3212))  # 印出 9414
print(square_digits(2112))  # 印出 4114
print(square_digits(387))  # 印出 96449
