S = input()

T = ''

reverse = False

for i in range(len(S)):
    if (S[i] == 'R'):
        reverse = not reverse
    else:
        if (reverse):
            if (T and T[0] == S[i]):
                T = T[1:]
            else:
                T = S[i] + T
        else:
            if (T and T[-1] == S[i]):
                T = T[:-1]
            else:
                T = T + S[i]

if (reverse):
    T = T[::-1]

print(T)
