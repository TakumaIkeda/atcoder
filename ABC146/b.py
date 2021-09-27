n = int(input())
s = input()
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ans = ''
for i in s:
    ans += alphabets[(alphabets.index(i) + n) % 26]

print(ans)
