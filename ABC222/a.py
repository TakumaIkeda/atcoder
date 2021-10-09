import sys

n = sys.stdin.readline().strip()
length = len(n)

ans = ""
for i in range(4 - length):
    ans += "0"
ans += str(n)

print(ans)
