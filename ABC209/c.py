N = int(input())
C = sorted(list(map(int, input().split())))

sum = 0
rest = 0
count = 1
for i in range(len(C)):
  rest = C[i] - sum
  if (rest < 0):
    count = 0
    break
  count = (count * rest) % (10 ** 9 + 7)
  sum += 1

print(count % (10**9+7))