import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().strip().split()))

able = set()

for i in range(143):
    for j in range(143):
        able.add(4 * (i + 1) * (j + 1) + 3 * (i + 1) + 3 * (j + 1))

cnt = 0
for i in s:
    if not i in able:
        cnt += 1

print(cnt)
