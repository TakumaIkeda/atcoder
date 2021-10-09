import sys
import numpy as np

n, m = map(int, sys.stdin.readline().strip().split())
hands = []

janken = {'G': 0, 'C': 1, 'P': 2}

for i in range(2 * n):
    hands.append(sys.stdin.readline().strip())

dp = [[0 for _ in range(2 * n)] for _ in range(m + 1)]
for i in range(m):
    round = np.argsort(dp[i])
    for j in range(n):
        if (janken[hands[round[2 * j]][i]] - janken[hands[round[2 * j + 1]][i]]) % 3 == 2:
            dp[i + 1][round[2 * j]] = dp[i][round[2 * j]] + 1
            dp[i + 1][round[2 * j + 1]] = dp[i][round[2 * j + 1]]
        elif (janken[hands[round[2 * j]][i]] - janken[hands[round[2 * j + 1]][i]]) % 3 == 1:
            dp[i + 1][round[2 * j]] = dp[i][round[2 * j]]
            dp[i + 1][round[2 * j + 1]] = dp[i][round[2 * j + 1]] + 1
        else:
            dp[i + 1][round[2 * j]] = dp[i][round[2 * j]]
            dp[i + 1][round[2 * j + 1]] = dp[i][round[2 * j + 1]]

ans = np.array(dp[m])
ranking = np.sort(ans)[::-1]
i = 0
while True:
    idx = np.where(ans == ranking[i])[0]
    for j in idx:
        print(j + 1)
        ranking[i] = False
        i += 1

    if i == len(ans):
        break
