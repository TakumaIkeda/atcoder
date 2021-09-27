from math import gcd

A, B, C = map(int, input().split(' '))

AB = gcd(A, B)
ABC = gcd(AB, C)

print(A // ABC + B // ABC + C // ABC - 3)
