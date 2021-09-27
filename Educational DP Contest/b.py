n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [0] * n

for i in range(n-1):
    dp[i+1] = min([abs(h[i-j]-h[i+1])+dp[i-j] for j in range(min(k, i+1))])

print(dp[n-1])
