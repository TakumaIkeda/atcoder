A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0

for a in range(A + 1):
    rest = X - 500 * a
    if (rest == 0):
        count += 1
        continue
    elif(rest < 0):
        continue
    for b in range(B + 1):
        rest = X - 500 * a - 100 * b
        if (rest == 0):
            count += 1
            continue
        elif (rest < 0):
            continue
        for c in range(C + 1):
            rest = X - 500 * a - 100 * b - 50 * c
            if (rest == 0):
                count += 1
                continue
            elif(rest < 0):
                continue

print(count)
