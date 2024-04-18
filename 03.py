# 編號：CANDY-003
# 程式語言：Python
# 題目：完成函數的內容，把陣列裡的 0 都移到最後面


# list = [False, 1, 0, -1, 2, 0, 1, 3, "a"]

# def move_zeros_to_end(list):# 定義函數

#     zeros = [o for o in list if o == 0 and o is not False] # 收集 0 以及不是 False
#     out_of_zeros = [x for x in list if x != 0 or x is False] # 收集 False 跟 0 以外的元素
#     return out_of_zeros + zeros # 兩者相結合
    
    
# result = move_zeros_to_end(list)
# print(result)


data = [False, 1, 0, -1, 2, 0, 1, 3, "a"]

result = [n for n in data if n == 0 and not isinstance(False,int)]
print(result)