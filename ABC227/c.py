import sys
import math

n = int(sys.stdin.readline())

a, b, c = 1, 1, 1
cnt = 0
for a in range(1, n + 1):
    if a ** 3 > n:
        break
    for b in range(a, n + 1):
        if a * (b ** 2) > n:
            break
        cnt += n // (a * b) - b + 1

print(cnt)
