from math import floor


def hantei(value, A, B):
    thousand = floor(value / 1000)
    hundred = floor((value - thousand * 1000) / 100)
    ten = floor((value - thousand * 1000 - hundred * 100) / 10)
    one = value - thousand * 1000 - hundred * 100 - ten * 10
    sum = thousand + hundred + ten + one
    return A <= sum and sum <= B


N, A, B = input().split(' ')
N = int(N)
A = int(A)
B = int(B)

sum = 0

for i in range(N):
    if (hantei(i + 1, A, B)):
        sum += i + 1

print(sum)
