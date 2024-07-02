# 編號：CANDY-018
# 程式語言：Python
# 題目：實作一個可以印出隨機整數的函數

import random


def random_number(*num):
    if len(num) not in [1, 2]:
        raise ValueError("請給一個或兩個數字！")

    start, end = (0, num[0]) if len(num) == 1 else (num[0], num[1])

    return random.randint(start, end - 1)


print(random_number(50))
# 隨機印出 0 ~ 49 之間的任何一個數字
print(random_number(5, 30))
# 隨機印出 5 ~ 29 之間的任何一個數字
