import sys

s = sys.stdin.readline()
t = sys.stdin.readline()

for i in range(len(s) - 1):
    if s[0:i] + s[i + 1] + s[i] + s[i+2:] == t:
        print("Yes")
        exit()
    elif s == t:
        print('Yes')
        exit()

print("No")
