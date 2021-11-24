n, k = map(int, input().split())
p = []

for i in range(n):
    p.append(list(map(int, input().split())))

psum = list(map(sum, p))
pk = sorted(psum, reverse=True)[k-1]

for i in psum:
    if i + 300 >= pk:
        print('Yes')
    else:
        print('No')
