import itertools

s, k = input().split()
k = int(k)

res = sorted(list(set(itertools.permutations(sorted(s), len(s)))))[k - 1]
print(''.join(res))
