import math

n = int(input())
a = list(map(int, input().split()))

ans = a[0]

for i in range(n):
    ans = math.gcd(ans, a[i])


print(ans)
