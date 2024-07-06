# 編號：CANDY-019
# 程式語言：Python
# 題目：檢查是否為某個數字的平方數

import math


def is_square(number):
    if number < 0:
        return False
    sqrt = math.sqrt(number)
    return sqrt.is_integer()


print(is_square(0))
# true
print(is_square(4))
# true
print(is_square(5))
# false
print(is_square(100))
# true
print(is_square(-4))
# false
print(is_square(-1))
# false
