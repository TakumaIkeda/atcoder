import sys

a, b, c = map(int, sys.stdin.readline().split())

i = 0
while b >= c * i:
    if (a <= c * i and c * i <= b):
        print(c * i)
        exit()
    i += 1

print(-1)
