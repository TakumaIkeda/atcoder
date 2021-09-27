# coding: utf-8
# Your code here!

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
        input = """6
1 123 12345 12 1234 123456"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
3 1 4 15 9"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    a_sort = sorted(a)

    b = a_sort[-2]
    print(a.index(b)+1)
