N = input()

for i in N:
  if (N[-1] == '0'):
    N = N[:len(N) - 1]
  else:
    break

new_str = ''

for i in N:
  new_str = i + new_str

if (new_str == N):
  print('Yes')
else:
  print('No')
