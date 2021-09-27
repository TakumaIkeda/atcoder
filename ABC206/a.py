from math import floor

N = int(input())

tax_included = floor(N * 1.08)

if (tax_included < 206):
  print('Yay!')
elif (tax_included == 206):
  print('so-so')
else:
  print(':(')