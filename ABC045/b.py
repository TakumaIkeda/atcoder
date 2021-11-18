sa = input()
sb = input()
sc = input()

now = 0
cnta = 0
cntb = 0
cntc = 0
while True:
    if now == 0:
        if cnta == len(sa):
            print('A')
            break
        if sa[cnta] == 'a':
            now = 0
        if sa[cnta] == 'b':
            now = 1
        if sa[cnta] == 'c':
            now = 2
        cnta += 1
    if now == 1:
        if cntb == len(sb):
            print('B')
            break
        if sb[cntb] == 'a':
            now = 0
        if sb[cntb] == 'b':
            now = 1
        if sb[cntb] == 'c':
            now = 2
        cntb += 1
    if now == 2:
        if cntc == len(sc):
            print('C')
            break
        if sc[cntc] == 'a':
            now = 0
        if sc[cntc] == 'b':
            now = 1
        if sc[cntc] == 'c':
            now = 2
        cntc += 1
