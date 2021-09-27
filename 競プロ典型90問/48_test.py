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
        input = """4 3
4 3
9 5
15 8
8 6"""
        output = """21"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2
7 6
3 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 12
987753612 748826789
36950727 36005047
961239509 808587458
905633062 623962559
940964276 685396947
959540552 928301562
60467784 37828572
953685176 482123245
87983282 66762644
912605260 709048491"""
        output = """6437530406"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
    n, k = map(int, input().split())
    a, b = [], []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [0 for _ in range(n)]
    for _ in range(n):
