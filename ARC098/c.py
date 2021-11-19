n = int(input())
s = input()

cnt = 0
for i in range(n-1):
    if s[i+1] == 'E':
        cnt += 1

mn = cnt
for i in range(n-1):
    if s[i] == 'W':
        cnt += 1
    if s[i+1] == 'E':
        cnt -= 1

    if mn > cnt:
        mn = cnt

print(mn)
