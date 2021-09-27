s = input()
t = input()

dp = [[None for _ in range(len(s))] for _ in range(len(t)+1)]
for i in range(len(s)):
    dp[0][i] = 0

for i in range(len(t)):
    found = False
    found2 = False

    if (sum(dp[i]) == 0):
        found = True
    for j in range(len(s)):
        if (found2):
            dp[i+1][j] = 0
        elif (dp[i][j] == 1):
            dp[i+1][j] = 1
            found = True
        elif (found and s[j] == t[i]):
            dp[i+1][j] = 1
            found2 = True
        else:
            dp[i+1][j] = 0

string = ''
for i in range(len(s)):
    if (dp[len(t)][i] == 1):
        string += s[i]

print(string)
