N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_len = [0 for i in range(N)]
B_len = [[] for i in range(N)]
C_len = [0 for i in range(N)]

for i in range(N):
    A_len[A[i] - 1] += 1
    B_len[B[i] - 1].append(i)
    C_len[C[i] - 1] += 1

count = 0

for i in range(N):
    if (A_len[i] == 0 or B_len[i] == 0):
        continue
    B_idx = sum(list(map(lambda e: C_len[e], B_len[i])))
    count += A_len[i] * B_idx

print(count)
