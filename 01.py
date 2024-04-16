#  編號：CANDY- 001
#  程式語言：Python
#  題目：找出列表裡最小的兩個值的總和
#  例如：
#  [15, 28, 4, 2, 43] 印出 6
#  [23, 71, 33, 82, 1] 印出 24

def sum_of_smallest_values(input): # 定義一個函數將列表內最小兩個值加總
    if len(input) < 2:   # 如果傳入列表長度小於2，表示只有一個數字，無法進行運算，回傳None
        return None
    
    sorted_list = sorted(input) # 將進行排序後的列表依序賦值
    return sorted_list[0] + sorted_list[1] # 回傳賦值後列表其索引值0,1，表示最小兩個

list1 = [19, 5, 42, 2, 77]      # 分別定義列表
list2 = [23, 15, 59, 4, 17]

print(sum_of_smallest_values(list1))      #依序印出
print(sum_of_smallest_values(list2))
