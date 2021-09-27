n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = 0
combination_x = []

for i in range(n):
    for j in range(i + 1, n):
        if (x[i] == x[j]):
            combination_x.append([i, j])

for i in range(len(combination_x)):
    for j in range(i + 1, len(combination_x)):
        if (y[combination_x[i][0]] == y[combination_x[j][0]] and y[combination_x[i][1]] == y[combination_x[j][1]]):
            ans += 1

print(ans)
