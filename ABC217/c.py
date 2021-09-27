n = int(input())
p = list(map(int, input().split()))

sol = [0 for _ in range(n)]

for i in range(len(p)):
    sol[p[i]-1] = i + 1

sol = list(map(str, sol))
print(' '.join(sol))
