import sys
import math

n = int(sys.stdin.readline().strip())
xy = []
magics = []


for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    xy.append([x, y])

for i in range(n):
  for j in range(n):
    if i == j: continue
    dx = xy[i][0] - xy[j][0]
    dy = xy[i][1] - xy[j][1]
    gcd = math.gcd(dx, dy)
    dx /= gcd
    dy /= gcd
    magics.append([dx, dy])

magics = sorted(magics)

cnt = 1
for i in range(len(magics) - 1):
  if magics[i + 1] != magics[i]:
    cnt += 1

print(cnt)