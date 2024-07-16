# 編號：CANDY-023
# 程式語言：Python
# 題目：算出 N 個數字的最大公因素
import math
from functools import reduce


def calc_gcd(*numbers):
    return reduce(math.gcd, numbers)


print(calc_gcd(10))
# 10
print(calc_gcd(103, 27))
# 1
print(calc_gcd(104, 96, 36, 88))
# 4
