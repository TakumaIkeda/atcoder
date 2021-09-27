H, W = map(int, input().split(' '))
A = [list(map(int, input().split(' '))) for i in range(H)]
B = A

row_sum = [0 for i in range(H)]
col_sum = [0 for i in range(W)]

for i in range(H):
    row_sum[i] += sum(A[i])
    for j in range(W):
        col_sum[j] += A[i][j]

for i in range(H):
    for j in range(W):
        B[i][j] = str(row_sum[i] + col_sum[j] - A[i][j])

for i in range(H):
    print(' '.join(B[i]))
