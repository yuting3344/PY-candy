# 編號：CANDY-014
# 程式語言：Python
# 題目：把鄰近的重複值去除，但仍照原本的順序排序
# 範例："AAABBBDDDAABBBCC" -> ['A', 'B', 'D', 'A', 'B', 'C']


def unique_order(seq):
    if not seq:  # 解釋是否為空字串
        return []

    result = [seq[0]]  # 將字串第一個元素放進 result 列表，初始化

    for i in range(1, len(seq)):  # 前後比較，不重複 append 進結果列表
        if seq[i] != seq[i - 1]:
            result.append(seq[i])
    return result


print(unique_order("AABCC"))
# [ 'A', 'B', 'C']
print(unique_order("AAABBBCCBCC"))
# [ 'A', 'B', 'C', 'B', 'C']
print(unique_order([1, 2, 1, 2, 1]))
# [ 1, 2, 1, 2, 1 ]
print(unique_order([1, 1, 1, 2, 2, 2, 1]))
# [1, 2, 1]
