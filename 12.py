# 編號：CANDY-012
# 程式語言：Python
# 題目：把數字加總，最終濃縮成個位數
# 範例：9527 => 9 + 5 + 2 + 7 => 23 => 2 + 3 => 5
#      1450 => 1 + 4 + 5 + 0 => 10 => 1 + 0 => 1


def number_reduce(num):
    while num >= 10:
        num = sum([int(dig) for dig in str(num)])
    return num


print(number_reduce(9527))
# 印出 5
print(number_reduce(1450))
# 印出 1
print(number_reduce(5566108))
# 印出 4
print(number_reduce(1234567890))
# 印出 9


# if num < 10:
#         return num
#     else:
#         return number_reduce(sum([int(dig) for dig in str(num)]))
