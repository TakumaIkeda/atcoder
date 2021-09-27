N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

count = 0

for x in range(1000):
    right = True
    for i in range(N):
        if (not(A[i] <= x + 1 and x + 1 <= B[i])):
            right = False
    if (right):
        count += 1

print(count)
