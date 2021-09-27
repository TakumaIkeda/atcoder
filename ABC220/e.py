import sys

n, d = map(int, sys.stdin.readline().split())

cnt = 0
for i in range(n):
    for j in range(i+1):
        cnt += 2**(n-j) // 2**(n-i)

print(cnt)
