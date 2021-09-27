from math import floor

N, K = map(int, input().split())
a = list(map(int, input().split()))
a_sorted = sorted(a)

mod_n = K % N
n_divide = floor(K / N)

a_K = a_sorted[mod_n - 1]

for i in a:
  if (i <= a_K and (not mod_n == 0)):
    print(n_divide + 1)
  else:
    print(n_divide)
