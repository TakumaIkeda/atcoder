n = int(input())
x, y = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())


dp = [[[0 for _ in range(x + 1)] for _ in range(y + 1)]
      for _ in range(n)]

# 1品目を食べるか食べないか
for j in range(x + 1):
    for k in range(y + 1):
        if a[0] < j and b[0] < k:
            dp[0][j] = cost_list[0]  # 食べるとき

# 2品目以降を食べるか食べないか
for i in range(1, list_len):
    for j in range(limit + 1):
        tmp_not_choice = dp_table[i-1][j]
        if kcal_list[i] > j:  # カロリーオーバー
            dp_table[i][j] = tmp_not_choice  # 食べられない
        else:
            tmp_choice = dp_table[i-1][j - kcal_list[i]] + cost_list[i]
            dp_table[i][j] = max(tmp_choice, tmp_not_choice)
# dp = [[[0 for _ in range(x)] for _ in range(y)] for _ in range(n + 1)]
# for i in range(n):
#     a, b = map(int, input().split())
#     ab.append([a, b])

# for i in range(y):
#     for j in range(x):
#         if (ab[0][0] > j + 1 and ab[0][1] > i + 1):
#             dp[0][i][j] = 1
# for i in range(n - 1):
#     a = ab[i][0]
#     b = ab[i][1]
#     for j in range(y):
#         for k in range(x):
#             dp[i + 1][j][k] = min(dp[i][j - b]
#                                   [k - a] - 1, dp[i][j + 1][k + 1])

# print(dp)
