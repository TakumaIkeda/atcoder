S = input()
maru = set()
hatena = set()
batu = set()

for i in range(len(S)):
  if (S[i] == 'o'):
    maru.add(i)
  elif (S[i] == '?'):
    hatena.add(i)
  else:
    batu.add(i)

already = set()

for i in range(10):
  if (i in batu):
    continue
  for j in range(10):
    if (j in batu):
      continue
    for k in range(10):
      if (k in batu):
        continue
      for l in range(10):
        if (l in batu):
          continue
        maru_filtered = list(filter(lambda e: not (e == i or e == j or e == k or e == l), maru))
        if (len(maru_filtered) == 0 and not (str('{}{}{}{}'.format(i, j, k, l)) in already)):
          already.add(str('{}{}{}{}'.format(i, j, k, l)))

print(len(already))
