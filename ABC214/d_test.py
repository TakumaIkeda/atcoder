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
1 2 10
2 3 20"""
        output = """50"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2 1
2 3 2
4 2 5
3 5 14"""
        output = """76"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
    n = int(input())
