# 編號：CANDY-017
# 程式語言：Python
# 題目：計算數字的 2 進位裡有幾個 1
# 範例：5 -> 101 -> 2 個 1


def count_bits(decimal_num):
    binary_num = bin(decimal_num)
    count_of_ones = binary_num.count("1")
    return count_of_ones


print(count_bits(1234))
# 5
print(count_bits(1450))
# 6
print(count_bits(9527))
# 8
