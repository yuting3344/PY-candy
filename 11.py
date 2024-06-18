# 編號：CANDY-011
# 程式語言：Python
# 題目：找出一個數字串列裡，出現奇數次數的數字
# 範例：[1, 1, 0]，`0` 只有出現 1 次
#      [5, 5, 8, 8, 8, 4, 4]，`8` 出現了 3  次


def find_odd_elm(numbers):
    for num in numbers:
        if numbers.count(num) % 2 != 0:
            return num


print(find_odd_elm([1, 1, 2]))
# 印出 2
print(find_odd_elm([5, 4, 2, 1, 5, 4, 2, 10, 10]))
# 印出 1
print(find_odd_elm([0, 1, 0, 1, 0]))
# 印出 0
print(find_odd_elm([1, 1, 2, -2, 5, 2, -1, -2, 5]))
# 印出 -1
print(find_odd_elm([20, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
# 印出 5
