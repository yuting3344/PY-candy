# 編號：CANDY-016
# 程式語言：Python
# 題目：把原本 snake_case 的字轉換成 camelCase 格式
# 範例："hello_world" -> "helloWorld"


def to_camel_case(string):

    split_str = string.split("_")

    words = [word.capitalize() for word in split_str]

    camel_case_str = "".join(words)

    return camel_case_str[0].lower() + camel_case_str[1:]


print(to_camel_case("book"))
# book
print(to_camel_case("book_store"))
# bookStore
print(to_camel_case("get_good_score"))
# getGoodScore
