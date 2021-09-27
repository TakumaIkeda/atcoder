from collections import deque

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """4 5
1 2
1 3
3 2
2 4
3 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 3
2 3
4 5
5 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 8
5 3
2 3
2 4
5 2
5 1
1 4
4 3
1 3"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
    class Node:
        def __init__(self):
            self.come = []
            self.go = []
            self.come_len = 0
            self.go_len = 0
            self.searched = False
    
    n, m = map(int, input().split())
    nodes = [Node() for _ in range(m + 1)]
    que = deque()
    for _ in range(m):
        x, y = map(int, input().split())
        nodes[x].go.append(y)
        nodes[y].come.append(x)

    for i in range(m):
        if (len(nodes[i+1].come) == 0):
            que.append(nodes[i+1])
            nodes[i+1].searched = True
    
    while (not all(map(lambda e: e.searched, nodes))):
        while (len(que) > 0):
        