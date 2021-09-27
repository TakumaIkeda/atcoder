n, w = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
dp = []

dp.append([0]*(w+1))
for i in range(n):
    dp.append([0])
    for j in range(w):
        if (j+1-ls[i][0] >= 0):
            dp[i+1].append(max(dp[i][j+1-ls[i][0]]+ls[i][1], dp[i][j+1]))
        else:
            dp[i+1].append(dp[i][j+1])
print(dp[n][w])
