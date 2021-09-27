N = int(input())
A, B, C = sorted(list(map(int, input().split(' '))))
count = 10000

for i in range(10000):
    for j in range(10000 - i):
        C_count = (N - i * A - j * B) // C
        if (count < i + j + C_count):
            break
        if ((N - (i * A + j * B)) % C == 0 and count > i + j + C_count):
            count = i + j + C_count
            break

print(count)
