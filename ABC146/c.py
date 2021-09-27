a, b, x = map(int, input().split())


def isOk(index, key):
    return a * index + b * len(str(index)) > key


def binary_search(key):
    ng = -1
    ok = 10**9+1
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if (isOk(mid, key)):
            ok = mid
        else:
            ng = mid
    return ok


print(max(binary_search(x)-1, 0))
