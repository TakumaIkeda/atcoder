n = int(input())
names = []
flg = False
for i in range(n):
    s, t = input().split()
    names.append([s, t])

for i in range(n):
    for j in range(n):
        if (i == j):
            continue
        if (names[i][0] == names[j][0] and names[i][1] == names[j][1]):
            flg = True
            break

if (flg):
    print("Yes")
else:
    print("No")
