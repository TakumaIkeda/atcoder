s = input()
k = int(input())
n = len(s)
memo = [0 for _ in range(len(s))]
now = 0

flg = True
for i in range(n):
    if s[i] == '.':
        now += 1
    memo[i] = now


def isOk(array, index, key, idx):
    return array[index] - array[idx] <= key


def binary_search(array, idx, key):
    ok = idx - 1
    ng = len(array)
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if (isOk(array, mid, key, idx)):
            ok = mid
        else:
            ng = mid
    return ok


ans = 0
for i in range(n):
    key = binary_search(memo, i, k)
    if key - i >= ans:
        ans = key - i

print(ans)
