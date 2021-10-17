import sys
from decimal import Decimal

n = int(sys.stdin.readline())
time = 0
a = []
b = []

for i in range(n):
    ai, bi = map(Decimal, sys.stdin.readline().split())
    time += ai / bi
    a.append(ai)
    b.append(bi)

half = time / 2
cnt = 0
length = 0
while True:
    half -= a[cnt] / b[cnt]
    length += a[cnt]
    if (half < 0):
        half += a[cnt] / b[cnt]
        length -= a[cnt]
        length += b[cnt] * half
        break
    cnt += 1

print(length)
