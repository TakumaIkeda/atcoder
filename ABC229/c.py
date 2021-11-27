n, w = map(int, input().split())

arr = []
a, b = [], []
for i in range(n):
    ai, bi = map(int, input().split())
    arr.append([ai, i])
    a.append(ai)
    b.append(bi)

arr.sort(reverse=True)
sum = 0
ans = 0
i = 0
while sum <= w and i < n:
    sum += b[arr[i][1]]
    ans += a[arr[i][1]] * b[arr[i][1]]
    i += 1

if sum > w:
    ans -= a[arr[i-1][1]] * (sum - w)

print(ans)
