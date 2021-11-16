n = int(input())
a = list(map(int, input().split()))

arr = []
for i in range(n):
    arr.append([a[i], i+1])

arr.sort(reverse=True)

for i in range(n):
    print(arr[i][1])
