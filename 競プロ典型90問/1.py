import itertools

N, L = input().split(' ')
K = input()
A = input().split(' ')

N = int(N)
L = int(L)
K = int(K)
for i in range(len(A)):
    A[i] = int(A[i])

score = 0

combinations = list(itertools.combinations(A, K))
for i in range(len(combinations)):
    yokans = combinations[i]
    min_piece = pow(10, 9)
    yokans_length = len(yokans)
    for j in range(yokans_length + 1):
        if (j == 0):
            min_piece = yokans[0]
            continue
        if (j == yokans_length):
            if (L - yokans[yokans_length - 1] < min_piece):
                min_piece = L - yokans[yokans_length - 1]
            continue
        if (yokans[j] - yokans[j - 1] < min_piece):
            min_piece = yokans[j] - yokans[j - 1]
    print(min_piece)
    if (score < min_piece):
        score = min_piece


print(score)
