mod = 10 ** 9 + 7
s = input()
c = ch = cho = chok = choku = chokud = chokuda = chokudai = 0

for char in s:
    if char == 'c':
        c += 1
    elif char == 'h':
        ch += c
    elif char == 'o':
        cho += ch
    elif char == 'k':
        chok += cho
    elif char == 'u':
        choku += chok
    elif char == 'd':
        chokud += choku
    elif char == 'a':
        chokuda += chokud
    elif char == 'i':
        chokudai += chokuda

print(chokudai % mod)
