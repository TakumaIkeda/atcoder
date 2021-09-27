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

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(list(map(int, input().split())))

minimum = 10**9+10

for i in a:
  solv = binary_search(b, i)
  if (solv != m):
    if (abs(b[solv] - i) < minimum):
      minimum = abs(b[solv] - i)
    elif(solv != 0):
      if (abs(b[solv-1] - i) < minimum):
        minimum = abs(b[solv-1] - i)
  else:
    if (abs(b[solv-1] - i) < minimum):
      minimum = abs(b[solv-1] - i)


print(minimum)