N = int(input())

for i in range(2 ** N):
    line = ""
    count = 0
    for j in range(N):
        if ((i >> j) & 1 == 1):
            line = ")" + line
            count -= 1
        else:
            line = "(" + line
            count += 1
        if (count > 0):
            break
    if (count != 0):
        continue
    else:
        print(line)
