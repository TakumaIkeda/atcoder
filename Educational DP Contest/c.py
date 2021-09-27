n = int(input())
actions = []
dp = []
for _ in range(n):
    actions.append(list(map(int, input().split())))

dp.append(actions[0])
for i in range(n-1):
    dp.append([max(dp[i][1], dp[i][2]) + actions[i+1][0],
              max(dp[i][0], dp[i][2]) + actions[i+1][1],
              max(dp[i][0], dp[i][1]) + actions[i+1][2]])

print(max(dp[n-1]))
