import itertools
import sys

n = sys.stdin.readline().strip()

memo = 0
for i in range(len(n) - 1):
    com = list(itertools.combinations(n, i + 1))
    for j in com:
        num1 = ''.join(sorted(j, reverse=True))
        num2 = n
        for k in j:
            idx = num2.index(k)
            num2 = num2[:idx] + num2[idx + 1:]

        num1 = int(num1)
        num2 = int(''.join(sorted(num2, reverse=True)))
        if num1 * num2 > memo:
            memo = num1 * num2

print(memo)
