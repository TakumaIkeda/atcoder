A1, A2, A3 = sorted(list(map(int, input().split())))

if (A3 - A2 == A2 - A1):
  print('Yes')
else:
  print('No')