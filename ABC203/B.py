N, K = map(int, input().split())

count = 0
for i in range(N):
  for j in range(K):
    count += 100 * (i + 1) + (j + 1)

print(count)