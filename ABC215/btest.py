n = int(input())
flag = False
cnt = 0
while True:
    if (2 ** cnt > n):
        break
    cnt += 1

print(cnt - 1)
