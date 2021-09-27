N = int(input())
A = list(map(int, input().split()))
S = set()
A_sorted = sorted(A)

count = len(A) * (len(A) - 1) / 2

same_count = 0
for i in range(len(A_sorted)):
  if (i == 0):
    same_count += 1
    continue
  if (A_sorted[i] == A_sorted[i - 1]):
    same_count += 1
    continue
  count -= same_count * (same_count - 1) / 2
  same_count = 1

count -= same_count * (same_count - 1) / 2
same_count = 0

print(int(count))
