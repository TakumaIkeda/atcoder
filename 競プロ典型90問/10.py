N = int(input())
scores1 = [0]
scores2 = [0]
for i in range(N):
    C, P = map(int, input().split(' '))
    if (C == 1):
        scores1.append(scores1[-1] + P)
        scores2.append(scores2[-1])
        continue
    scores1.append(scores1[-1])
    scores2.append(scores2[-1] + P)

Q = int(input())

for i in range(Q):
    L, R = map(int, input().split(' '))
    print(scores1[R] - scores1[L-1], scores2[R] - scores2[L-1])
