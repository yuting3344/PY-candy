# 編號：CANDY-004
# 程式語言：Python
# 題目：完成函數的內容，把傳進去的秒數變成平常人類看的懂的時間格式


def human_readable_timer(seconds):  # 定義函數
    hours = seconds // 3600  # 傳入數字整除3600，表示時
    minutes = (seconds % 3600) // 60  # 對3600取餘數，整除60，表示分
    seconds = seconds % 60  # # 傳入數字對60取餘數，表示秒
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    # 02d 表示：
    # 1. 02 : 填滿到兩個數寬度，用0為前導
    # 2. d : 將整數格式化為至少兩位寬度的十進位數


print(human_readable_timer(0))
# 印出 00:00:00
print(human_readable_timer(59))
# 印出 00:00:59
print(human_readable_timer(60))
# 印出 00:01:00
print(human_readable_timer(90))
# 印出 00:01:30
print(human_readable_timer(3599))
# 印出 00:59:59
print(human_readable_timer(3600))
# 印出 01:00:00
print(human_readable_timer(45296))
# 印出 12:34:56
print(human_readable_timer(86399))
# 印出 23:59:59
print(human_readable_timer(86400))
# 印出 24:00:00
print(human_readable_timer(359999))
# 印出 99:59:59
