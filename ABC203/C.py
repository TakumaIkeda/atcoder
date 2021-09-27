N, K = map(int, input().split())
money = {}
for i in range(N):
  A, B = map(int, input().split())
  if (A in money):
    money[A] += B
  else:
    money[A] = B

money_keys = sorted(money.keys())
now = 0
for i in money_keys:
  if (i - now > K):
    now += K
    K = 0
    break
  else:
    now = i
    K -= i - now
    K += money[i]

if (K != 0):
  now += K - now

print(now)
