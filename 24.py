# 編號：CANDY-024
# 程式語言：Python
# 題目：算出 N 個數字的最小公倍數
# 提示：可使用 023 計算最大公因數的函數

import math
from functools import reduce


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def calc_lcm(*numbers):
    return reduce(lcm, numbers)


print(calc_lcm(10))
# 10
print(calc_lcm(103, 27))
# 2781
print(calc_lcm(21, 15, 18))
# 630
print(calc_lcm(104, 96, 36, 88))
# 41184
