import sys
s = sys.stdin.readline().strip()
smin = s
smax = s
now = s

for i in range(len(s)):
    now = now[1:] + now[0]
    if smin > now:
        smin = now

    if smax < now:
        smax = now

print(smin)
print(smax)
