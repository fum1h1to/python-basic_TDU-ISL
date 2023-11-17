# 素数のリスト prime_numbers があります。
prime_numbers = [2, 3, 5, 7]

# for 文を使って、0 ~ 10 の整数のうち、
# prime_numbers に含まれていない数字の合計値を出力してみよう。
sum = 0
for i in range(0, 11):
    if i not in prime_numbers:
        sum += i
print(sum)

# while 文を使って、上と同じことをしてみよう。
c = -1
sum = 0
while c < 10:
    c += 1
    if c in prime_numbers:
        continue
    sum += c
print(sum)