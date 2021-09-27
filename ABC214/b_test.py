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
        input = """1 0"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10"""
        output = """213"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """30 100"""
        output = """2471"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
    s, t = map(int, input().split())
    cnt = 0
    for i in range(s+1):
        for j in range(s-i+1):
            for k in range(s-i-j+1):
                if (i * j * k <= t):
                    cnt += 1

    print(cnt)
