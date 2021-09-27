import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for i in range(Q):
    E = int(input())
    y = -math.sin(E / T * math.pi * 2) * L / 2
    z = (1 - math.cos(E / T * math.pi * 2)) * L / 2
    distance = math.sqrt(X ** 2 + (Y - y) ** 2)
    print(math.atan2(z, distance) / math.pi * 180)
