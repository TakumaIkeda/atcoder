n, q = map(int, input().split())
a = [['N' for _ in range(n)] for _ in range(n)]
for i in range(q):
    s = list(map(int, input().split()))
    if (s[0] == 1):
        a[s[1] - 1][s[2] - 1] = 'Y'
    if (s[0] == 2):
        for j in range(n):
            if (a[j][s[1] - 1] == 'Y'):
                a[s[1] - 1][j] = 'Y'
    if (s[0] == 3):
        follow = []
        for j in range(n):
            if (a[s[1] - 1][j] == 'Y'):
                follow.append(j)
        for j in follow:
            for k in range(n):
                if (a[j][k] == 'Y'):
                    a[s[1] - 1][k] = 'Y'
for i in a:
    print(''.join(i))
