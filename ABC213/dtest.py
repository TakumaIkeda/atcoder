from collections import deque


class Node:
    def __init__(self):
        to = []
        sign = False


n = int(input())
nodes = [Node() for _ in range(n)]
for _ in range(n):
    a, b = map(int, input().split())
    nodes[a-1].to.append(b-1)
    nodes[b-1].to.append(a-1)

que = deque()
nodes[0].sign = True
que.append(nodes[0])
