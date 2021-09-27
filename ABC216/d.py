from collections import deque

n, m = map(int, input().split())
top = set()
colors = [0 for _ in range(n + 1)]
flg = False
a = []
aru = []
for i in range(m):
    k = int(input())
    ai = deque(map(int, input().split()))
    a.append(ai)
    elm = ai.popleft()
    if (not elm in top):
        top.add(elm)
        colors[elm] = i
    else:
        aru.append(elm)

if (len(aru) == 0):
    print('No')
    exit()

x = aru[0]
while True:
    idx = colors[x]
    atop = a[idx].popleft()
