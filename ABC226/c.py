import sys
from collections import deque

n = int(sys.stdin.readline().strip().strip())

abilities = []
times = []
already = set()
que = deque()


for i in range(n):
    ability = list(map(int, sys.stdin.readline().strip().split()))
    times.append(ability[0])
    abilities.append(ability[2:])

time = 0
already.add(n)
for i in abilities[-1]:
  que.append(i)
  already.add(i)
time += times[-1]

while len(que) > 0:
  ability = que.popleft()
  for i in abilities[ability - 1]:
    if i not in already:
      que.append(i)
      already.add(i)
  time += times[ability - 1]

print(time)