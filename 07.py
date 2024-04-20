# 編號：CANDY-007
# 程式語言：Python
# 題目：在某個數字串列裡，可能藏有某個不合群的奇數或偶數，試著找出它！


def find_some_different(numbers):
    even_count = sum(
        1 for num in numbers if num % 2 == 0
    )  # 生成器表達式來統計列表中偶數
    odd_count = len(numbers) - even_count  # 奇數 = 串列長度 - 偶數個數

    if even_count == 1:
        return next(
            item for item in numbers if item % 2 == 0
        )  # next 函數串列會找到可迭代物件中唯一數，無需遍歷串列
    else:
        return next(item for item in numbers if item % 2 != 0)


print(find_some_different([2, 4, 0, 100, 4, 11, 2602, 36]))
# 印出 11
print(find_some_different([160, 3, 1719, 19, 11, 13, -21]))
# 印出 160


# def find_some_different(numbers):
#     even_count = 0 #分別初始化數數器及數字
#     odd_count = 0
#     even_num = None
#     odd_num = None

#     for num in numbers:  # 設定條件，奇數跟偶數時加1，並更新數字
#         if num % 2 == 0:
#             even_count += 1
#             even_num = num
#         else:
#             odd_count += 1
#             odd_num = num

#     if even_count == 1:  # 如果其中一個計數器為1表示找到唯一數
#         return even_num
#     else:
#         return odd_num


# print(find_some_different([2, 4, 0, 100, 4, 11, 2602, 36]))
# # 印出 11
# print(find_some_different([160, 3, 1719, 19, 11, 13, -21]))
# # 印出 160
