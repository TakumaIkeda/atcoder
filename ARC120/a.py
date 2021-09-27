N = int(input())
a = list(map(int, input().split()))
arr = []

for i in range(N):
    arr.append(a[i])
    arr[-1] += max(arr)
    print(arr)
    print(sum(arr))
