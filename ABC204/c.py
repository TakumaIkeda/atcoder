from collections import deque

n, m = map(int, input().split())
routes = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    routes[a-1].append(b-1)

cnt = 0
for i in range(n):
  que = deque()
  already = set()
  already.add(i)
  que.append(i)
  while que:
    v = que.popleft()
    cnt += 1
    for j in routes[v]:
      if j not in already:
        already.add(j)
        que.append(j)

print(cnt)