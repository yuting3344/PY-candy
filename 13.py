# 編號：CANDY-013
# 程式語言：Python
# 題目：根據台灣財政部所提供的公司統編驗證規則，計算統一編號是否正確


def is_valid_vat_number(vat):
    if len(vat) != 8 or not vat.isdigit():  # 檢查是不是八位數，或者有無參雜非數字
        return False
    weights = [1, 2, 1, 2, 1, 2, 4, 1]  # 權重
    total = 0  # 定義初始權和變量

    for i in range(8):
        num = int(vat[i]) * weights[i]  # 將字串轉換為數字與權重列表相乘計算
        total += num // 10 + num % 10  # 計算十位數跟個位數相加的和

    return total % 10 == 0  # 如果可以整除 10 返回 True，否則 False


print(is_valid_vat_number("10458575"))  # True
print(is_valid_vat_number("88117125"))  # True
print(is_valid_vat_number("53212539"))  # True
print(is_valid_vat_number("88117126"))  # False
