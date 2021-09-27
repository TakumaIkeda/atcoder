import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

sum_a = sum(a)
rest = x % sum_a
loop = x // sum_a

flg = 0
count = 0
for i in a:
    flg += i
    count += 1
    if flg > rest:
        break

print(loop * len(a) + count)
