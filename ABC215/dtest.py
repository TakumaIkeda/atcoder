n, m = map(int, input().split())
a = list(map(int, input().split()))
k = set([i + 1 for i in range(m)])


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            while temp % i == 0:
                temp //= i
                arr.append(i)

    if temp != 1:
        arr.append(temp)

    if arr == []:
        arr.append(n)

    return arr


for i in a:
    fac = factorization(i)
    for j in fac:
        cnt = 1
        if (j in k and j != 1):
            while j * cnt <= m:
                if (j * cnt in k):
                    k.remove(j * cnt)
                cnt += 1

print(len(k))
for i in k:
    print(i)
