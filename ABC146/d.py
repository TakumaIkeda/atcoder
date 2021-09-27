from collections import deque


class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.color = 0
        self.sign = False


n = int(input())
nodes = [Node(i+1) for i in range(n)]
colors = [0 for _ in range(n-1)]
used = set()
for i in range(n-1):
    a, b = map(int, input().split())
    if (not b in nodes[a-1].nears):
        nodes[i].nears.append(b)

# dfs
q = deque()
q.append(nodes[0])
while q:
    node = q.pop()
    if node.sign:
        continue
    node.sign = True
    used_colors = set()
    used_colors.add(node.color)
    for near in node.nears:
        if not nodes[near-1].sign:
            q.append(nodes[near-1])
            col = 1
            while col in used_colors:
                col += 1
            nodes[near-1].color = col
            if not col in used:
                used.add(col)
            colors[near-2] = col

print(len(used))
for i in range(n-1):
    print(colors[i])
