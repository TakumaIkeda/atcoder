q = int(input())
balls = []

for i in range(q):
  p = x = 0
  query = list(map(int, input().split()))
  if (query[0] != 3):
    p = query[0]
    x = query[1]
  else:
    p = query[0]
  if (p == 1):
    balls.append(x)
  elif (p == 2):
    for i in range(len(balls)):
      balls[i] += x
  else:
    balls = sorted(balls, reverse=True)
    print(balls[-1])
    balls.pop()