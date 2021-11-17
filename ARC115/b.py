n = int(input())

c = []
for i in range(n):
    c.append(list(map(int, input().split())))

a = []
b = []
for i in range(n):
    a.append(c[i][0] - c[0][0])
    b.append(c[0][i])

flg = True
for i in range(n):
    for j in range(n):
        if (c[i][j] != a[i] + b[j]):
            flg = False

mn = min(a)
if mn < 0:
    a = list(map(lambda x: x - mn, a))
    b = list(map(lambda x: x + mn, b))

flg2 = True
for i in range(n):
    if b[i] < 0:
        flg2 = False

if flg and flg2:
    print('Yes')
    for i in range(n):
        print(a[i], end=' ')
    for i in range(n):
        print(b[i], end=' ')
else:
    print('No')
