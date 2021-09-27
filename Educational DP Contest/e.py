n, w = map(int, input().split())
weight = [None]*n
value = [None]*n

for i in range(n):
    wn, vn = map(int, input().split())
    weight[i] = wn
    value[i] = vn

MAX_VALUE = 10**5
MAX_WEIGHT = 10**12

dp = [[None for _ in range(MAX_VALUE+1)] for _ in range(n+1)]
for i in range(MAX_VALUE+1):
    dp[0][i] = MAX_WEIGHT

for i in range(n):
    dp[i][0] = 0
    for j in range(MAX_VALUE):
        if (j+1-value[i] < 0):
            dp[i+1][j+1] = dp[i][j+1]
        else:
            dp[i+1][j+1] = min(dp[i][j+1-value[i]]+weight[i], dp[i][j+1])

idx = MAX_VALUE
while(dp[n][idx] > w):
    idx -= 1
print(idx)
