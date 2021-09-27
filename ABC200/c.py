N = int(input())
A = list(map(lambda e: int(e) % 200, input().split(' ')))

count = 0

A = sorted(A)
A_item = 0
A_count = 0

for i in A:
    if (A_item != i):
        count += int(A_count * (A_count - 1) / 2)
        A_count = 0
        A_item = i
    A_count += 1

count += int(A_count * (A_count - 1) / 2)


print(count)
