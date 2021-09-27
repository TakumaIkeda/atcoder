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


N = int(input())
A = sorted(list(map(int, input().split(' '))))
Q = int(input())

for i in range(Q):
    B = int(input())
    index = binary_search(A, B)
    if (index > len(A) - 1):
        print(abs(A[len(A) - 1] - B))
        continue
    if (index == 0):
        print(abs(A[0] - B))
        continue
    if (A[index] - B > B - A[index - 1]):
        print(B - A[index - 1])
    else:
        print(A[index] - B)
