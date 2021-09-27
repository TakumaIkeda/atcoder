from math import ceil

A, B, C, D = map(int, input().split())

if (D * C - B > 0):
  print(ceil(A / (D * C - B)))
else:
  print(-1)