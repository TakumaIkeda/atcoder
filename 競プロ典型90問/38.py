import math

A, B = map(int, input().split())

gcd = math.gcd(A, B)

lcm = (A / gcd) * (B / gcd) * gcd

if (lcm > 10**18):
    print('Large')
else:
    print(int(lcm))
