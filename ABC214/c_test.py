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
        input = """3
4 1 5
3 10 100"""
        output = """3
7
8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
100 100 100 100
1 1 1 1"""
        output = """1
1
1
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 2 3 4
1 2 4 7"""
        output = """1
2
4
7"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8
84 87 78 16 94 36 87 93
50 22 63 28 91 60 64 27"""
        output = """50
22
63
28
44
60
64
27"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    dp = [0 for _ in range(n)]
    t_sort = sorted(t)
    idx = t.index(t_sort[0])

    for i in range(n):
        index = idx + i if (idx + i) < n else idx + i - n
        dp[index] = min(dp[index - 1] +
                        s[index - 1], t[index])

    for i in dp:
        print(i)
