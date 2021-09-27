n = int(input())
y = 0
flg = [False for _ in range(n)]
for i in range(n):
    a = int(input())
    if (flg[a - 1]):
        y = a
    flg[a - 1] = True

if (all(flg)):
    print('Correct')
else:
    print(y, flg.index(False) + 1)
