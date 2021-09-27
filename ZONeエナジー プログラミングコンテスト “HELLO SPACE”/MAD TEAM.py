import math
import itertools


N = int(input())
A = []
B = []
C = []
D = []
E = []
for i in range(N):
    value = input().split(' ')
    A.append(int(value[0]))
    B.append(int(value[1]))
    C.append(int(value[2]))
    D.append(int(value[3]))
    E.append(int(value[4]))


# def solve(M):

left = -1
right = 10 ** 9 + 1
while(right - left > 1):
    mid = math.floor(left + (right - left) / 2)
    if (solve(mid) == False):
        right = mid
    else:
        left = mid
