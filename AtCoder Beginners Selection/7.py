N = int(input())
a = input().split(' ')
a = sorted(list(map(lambda e: int(e), a)), reverse=True)

Alice = 0
Bob = 0

for i in range(len(a)):
    if (i % 2 == 0):
        Alice += a[i]
    else:
        Bob += a[i]

print(Alice - Bob)
