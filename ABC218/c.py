n = int(input())
s = []
t = []
s_not_sharp = [True for _ in range(n)]
t_not_sharp = [True for _ in range(n)]
for i in range(n):
    si = input()
    for j in range(n):
        if si[j] == '#':
            s_not_sharp[j] = False
    if (not all(j == '.' for j in si)):
        s.append(list(si))
for i in range(n):
    ti = input()
    for j in range(n):
        if ti[j] == '#':
            t_not_sharp[j] = False
    if (not all(j == '.' for j in ti)):
        t.append(list(ti))
s_cnt = 0
t_cnt = 0
for i in range(n):
    if s_not_sharp[i]:
        for j in range(len(s)):
            del s[j][i - s_cnt]
        s_cnt += 1
    else:
        break
for i in range(n):
    if t_not_sharp[i]:
        for j in range(len(t)):
            del t[j][i - t_cnt]
        t_cnt += 1
    else:
        break


for i in range(n):
    if s_not_sharp[i * -1 - 1]:
        for j in range(len(s)):
            del s[j][-1]
    else:
        break
for i in range(n):
    if t_not_sharp[i * -1 - 1]:
        for j in range(len(t)):
            del t[j][-1]
    else:
        break
s1 = [[s[len(s)-i-1][j] for i in range(len(s))] for j in range(len(s[0]))]
s2 = [[s1[len(s1)-i-1][j] for i in range(len(s1))]
      for j in range(len(s1[0]))]
s3 = [[s2[len(s2)-i-1][j] for i in range(len(s2))]
      for j in range(len(s2[0]))]

if (s == t or s1 == t or s2 == t or s3 == t):
    print('Yes')
else:
    print('No')
