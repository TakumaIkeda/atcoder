from collections import deque


class Node:
    def __init__(self, me):
        self.me = me
        self.to = []
        self.sign = 0


n, m = map(int, input().split())
nodes = [Node(i) for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    nodes[a].to.append(b)
    nodes[b].to.append(a)
queue = deque()
queue.append(nodes[1])

count = 0
while (queue):
    if (len(queue) == 0):
        break
    node = queue.popleft()
    if ():
        queue.appendleft(node)
        break

    for i in range(len(node.to)):
        if (not nodes[node.to[i]].sign or node.to[i] == n-1):
            nodes[node.to[i]].sign = node.sign + 1
            queue.append(nodes[node.to[i]])
        if (nodes[node.to[i]] == n):
            count = nodes[node.to[i]].sign

for i in range(len(queue)):
    node = queue.popleft()
    if (node.me == n):
        queue.append(node)

print(len(queue))
