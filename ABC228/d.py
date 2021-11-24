q = int(input())
a = [-1 for _ in range(2**20)]
s = set([i+1 for i in range(2**20)])
N = 2**20


def isOk(array, index, key):
    return array[index] >= key


def binary_search(array, key):
    ng = -1
    ok = len(array)
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if (isOk(array, mid, key)):
            ok = mid
        else:
            ng = mid
    return ok


for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        h = x
        mod = h % N
        key = binary_search(s, mod)
        mod = s[key] % N
        s[key] = N+10
        s.sort()
        a[mod-1] = x
    else:
        print(a[x % N-1])
