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
        input = """4
10 30 40 20"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
10 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
30 10 60 10 60 50"""
        output = """40"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
    n = int(input())
    h = list(map(int, input().split()))
    dp = [0] * n

    for i in range(n):
        if (i == 0):
            dp[i] = 0
        elif(i == 1):
            dp[i] = abs(h[i] - h[i-1])
        else:
            dp[i] = min(abs(h[i] - h[i-1]) + dp[i-1], abs(h[i] - h[i-2]) + dp[i-2])

    print(dp[n-1])
