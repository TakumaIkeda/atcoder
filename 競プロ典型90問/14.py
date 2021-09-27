N = int(input())
A = sorted(list(map(int, input().split(' '))))
B = sorted(list(map(int, input().split(' '))))

count = 0
for i in range(N):
    count += abs(A[i] - B[i])

print(count)
