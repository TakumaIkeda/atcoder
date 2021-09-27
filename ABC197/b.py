H, W, X, Y = map(int, input().split())
rows = []
count = 0
for i in range(H):
  rows.append(input())

i = 1
# 上向き
while (X - i >= 0):
  if (rows[X - i - 1][Y - 1] == '.'):
    count += 1
    i += 1
  else:
    break

i = 1
# 下向き
while (X + i <= W):
    if (rows[X + i - 1][Y - 1] == '.'):
      count += 1
      i += 1
    else:
      break

i = 1
# 右向き
while (Y + i <= H):
    if (rows[X - 1][Y + i - 1] == '.'):
      count += 1
      i += 1
    else:
      break

i = 1
# 左向き
while (Y - i >= 0):
    if (rows[X - 1][Y - i - 1] == '.'):
      count += 1
      i += 1
    else:
      break

print(count + 1)