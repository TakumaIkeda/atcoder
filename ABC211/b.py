s1 = input()
s2 = input()
s3 = input()
s4 = input()

s = sorted([s1, s2, s3, s4])

if (s[0] == '2B' and s[1] == '3B' and s[2] == 'H' and s[3] == 'HR'):
  print('Yes')
else:
  print('No')