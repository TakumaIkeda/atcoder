l, q = map(int, input().split())
cut = [0, l]


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
    c, x = map(int, input().split())
    if (c == 1):
        cut.append(x)
    else:
        # 高速にソート
        cut.sort()
        idx = binary_search(cut, x)
        print(cut[idx] - cut[idx - 1])
