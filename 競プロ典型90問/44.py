from collections import deque

N, Q = map(int, input().split())
A = deque(map(int, input().split()))
for i in range(Q):
    T, x, y = map(int, input().split())
    if (T == 1):
        Ax = A[x - 1]
        Ay = A[y - 1]
        A[x - 1] = Ay
        A[y - 1] = Ax
    elif (T == 2):
        A_last = A[-1]
        A.pop()
        A.appendleft(A_last)
    else:
        print(A[x - 1])
