#  編號：CANDY-002
#  程式語言：Python
#  題目：請寫一小段程式，印出連續串列裡缺少的字元


chars1 = ["a", "b", "c", "d", "f", "g"]
chars2 = ["O", "Q", "R", "S"]


def missing_char(chars): # 定義函數 missing_char
    
    unicode_list = [ord(n) for n in chars] # 遍歷傳入值中的元素，轉成unicode

    for i in range(len(unicode_list)-1): # 在迴圈中判斷前後相減是否為 -1，如果不是代表為串列缺口

          if unicode_list[i] - unicode_list[i+1] != -1:

            return chr(unicode_list[i]+1) # 回傳轉回英文的unicode
    
print((missing_char(chars1)))
print((missing_char(chars2)))
    











