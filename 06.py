# 編號：CANDY-006
# 程式語言：Python
# 題目：找出在數字串列裡跟其它元素不一樣的值

def find_different(numbers):

  unique_one = [n for n in numbers if numbers.count(n) == 1]

  return unique_one[0]


print(find_different([1, 1, 1, 1, 3, 1, 1, 1])); # 印出 3
print(find_different([2, 2, 2, 4, 2, 2])); # 印出 4
print(find_different([8, 3, 3, 3, 3, 3, 3, 3])); # 印出 8