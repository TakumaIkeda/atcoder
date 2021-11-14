import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

ok, ng = 0, 10**18 // k
while ng - ok > 1:
    md, sum = (ok + ng) // 2, 0
    for i in range(n):
        sum += min(a[i], md)
    if (sum >= k * md):
        ok = md
    else:
        ng = md


print(int(ok))
