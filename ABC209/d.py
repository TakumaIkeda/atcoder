N, Q = map(int, input().split())

class Node:
  def __init__(self, index):
    self.index = index
    self.nears = []
    self.sign = False
  def addNear(self, near):
    self.nears.append(near)
    self.nears = sorted(self.nears)

nodes = []
appendedNodes = set()

for i in range(N):
  nodes.append(Node(i + 1))

for i in range(N - 1):
  a, b = map(int, input().split())
  nodes[a - 1].addNear(b)
  nodes[b - 1].addNear(a)

for i in range(Q):
  c, d = map(int, input().split())
  count = 0
  while(True):

    if ()
    break
