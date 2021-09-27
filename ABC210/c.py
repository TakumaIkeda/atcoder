from collections import deque
N, K = map(int, input().split())
c = list(map(int, input().split()))

count = 0
queue = deque(c[0:K])
s = set(queue)
d = {}
for i in queue:
  if i in d:
    d[i] += 1
  else:
    d[i] = 1
count = len(d)
for i in range(N - K):
  left = queue.popleft()
  if (d[left] == 1):
    d.pop(left)
  else:
    d[left] -= 1
  now = c[K + i]
  queue.append(now)
  if (now in d):
    d[now] += 1
  else:
    d[now] = 1
  length = len(d)
  if (length > count):
    count = length

print(count)
