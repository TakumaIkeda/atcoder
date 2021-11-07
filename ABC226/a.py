import sys

x = sys.stdin.readline().strip()

i = 0
y = ''
while x[i] != '.':
    y += x[i]
    i += 1

y = int(y)

next = int(x[i + 1])
if (next < 5):
  print(y)
else:
  print(y + 1)