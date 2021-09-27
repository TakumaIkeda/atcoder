import sys

k = int(sys.stdin.readline())
a, b = sys.stdin.readline().split()

a10 = 0
b10 = 0

for i in range(len(a)):
    a10 += int(a[i]) * k ** (len(a) - i - 1)

for i in range(len(b)):
    b10 += int(b[i]) * k ** (len(b) - i - 1)

print(a10 * b10)
