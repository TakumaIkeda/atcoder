N = int(input())
S = list(input())
Q = int(input())
reverse = False
for i in range(Q):
    T, A, B = map(int, input().split(' '))
    if (T == 1):
        if (reverse):
            if (A < N and B < N):
                sa = S[N + A - 1]
                sb = S[N + B - 1]
                S[N + A - 1] = sb
                S[N + B - 1] = sa
            if (A < N and N <= B):
                sa = S[N + A - 1]
                sb = S[B - N - 1]
                S[N + A - 1] = sb
                S[B - N - 1] = sa
            if (N <= A and N <= B):
                sa = S[A - N - 1]
                sb = S[B - N - 1]
                S[A - N - 1] = sb
                S[B - N - 1] = sa
        else:
            sa = S[A - 1]
            sb = S[B - 1]
            S[A - 1] = sb
            S[B - 1] = sa
    if (T == 2):
        reverse = not reverse

if (reverse):
    front = S[:N]
    back = S[N:]
    S = back + front

print(''.join(S))
