s1 = input()
s2 = input()
s3 = input()
t = input()

ans = ''
for i in t:
    if (i == '1'):
        ans += s1
    elif (i == '2'):
        ans += s2
    else:
        ans += s3

print(ans)
