S = input()

count = 0

for i in range(len(S)):
    if (S[i] == 'Z' and S[i + 1] == 'O' and S[i + 2] == 'N' and S[i + 3] == 'e'):
        count += 1

print(count)
