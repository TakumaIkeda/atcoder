import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [[0 for _ in range(n)] for _ in range(10)]
dp[a[0]][0] = 1

for i in range(n - 1):
    for j in range(10):
        dp[(j + a[i+1]) % 10][i+1] = (dp[(j + a[i+1]) %
                                         10][i+1] + dp[j][i]) % 998244353
        dp[(j * a[i+1]) % 10][i+1] = (dp[(j * a[i+1]) %
                                         10][i+1] + dp[j][i]) % 998244353

for i in range(10):
    print(dp[i][n-1])
