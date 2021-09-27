x = list(input())
n = int(input())


def getStrNum(name):
    num = []
    for i in name:
        num.append(x.index(i))
    for i in range(10 - len(name)):
        num.append(-1)
    return num


ans = []
for i in range(n):
    s = input()
    ans.append(s)

ans = sorted(ans, key=getStrNum)

for i in ans:
    print(i)
