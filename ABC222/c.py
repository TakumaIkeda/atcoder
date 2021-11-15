import sys
n, m = map(int, sys.stdin.readline().split())

rank = [[0, i] for i in range(2*n)]

hand = [sys.stdin.readline().strip() for _ in range(2*n)]


def judge(i, j):
    if i == j:
        return -1
    if i == 'G' and j == 'C':
        return 0
    if i == 'C' and j == 'P':
        return 0
    if i == 'P' and j == 'G':
        return 0
    return 1


for j in range(m):
    for i in range(n):
        result = judge(hand[rank[2*i][1]][j], hand[rank[2*i+1][1]][j])
        if result != -1:
            rank[2*i+result][0] -= 1
    rank.sort()

for i in rank:
    print(i[1]+1)
