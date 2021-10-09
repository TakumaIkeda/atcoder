import sys

n, p = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))

print(len(list(filter(lambda x: x < p, a))))
