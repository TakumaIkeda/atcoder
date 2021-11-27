a, b = input().split()

flg = False
for i in range(min(len(a), len(b))):
    if int(a[-1*(i+1)]) + int(b[-1*(i+1)]) >= 10:
        flg = True

if flg:
    print('Hard')
else:
    print('Easy')
