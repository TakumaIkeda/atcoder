import sys

n, k, a = map(int, sys.stdin.readline().split())

person = a
for i in range(k - 1):
    person += 1
    if (person > n):
        person = 1

print(person)
