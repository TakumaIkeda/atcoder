import sys

n, m = map(int, sys.stdin.readline().strip().split())
p = [i + 1 for i in range(n)]
dic = {e + 1: v for v, e in enumerate([i for i in range(n)])}

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    if (dic[a] > dic[b]):
        p.pop(dic[b])
        p.insert(dic[a], b)
        dic[b] = dic[a]
