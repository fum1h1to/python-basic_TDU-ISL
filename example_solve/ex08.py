# コメント文を読み、print_string 関数を完成させよう。

def decorate_print(string):  # 引数の文字列を 10 回出力する関数
    print(string * 10)


def print_string(li, string):  # リストと文字列を受け取り、文字列を decorate_print に渡してリストを出力する関数
    # decorate_print に引数の文字列 string を渡す
    decorate_print(string)

    # リストの要素を、先頭に 1 から順番に番号と ":" をつけながら一行ずつ表示する
    for i, value in enumerate(li):
        print(str(i+1) + ':' + value)


my_list = ["print", "variable", "if", "list", "for"]
print_string(my_list, "*")

# 以下のように表示される
# **********
# 1:print
# 2:variable
# 3:if
# 4:list
# 5:for