import sys
from io import StringIO
import unittest


# class TestClass(unittest.TestCase):
#     def assertIO(self, input, output):
#         stdout, stdin = sys.stdout, sys.stdin
#         sys.stdout, sys.stdin = StringIO(), StringIO(input)
#         resolve()
#         sys.stdout.seek(0)
#         out = sys.stdout.read()[:-1]
#         sys.stdout, sys.stdin = stdout, stdin
#         self.assertEqual(out, output)

#     def test_入力例_1(self):
#         input = """4 5 2
# 3 2
# 2 5"""
#         output = """2 1
# 1 2"""
#         self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """1000000000 1000000000 10
# 1 1
# 10 10
# 100 100
# 1000 1000
# 10000 10000
# 100000 100000
# 1000000 1000000
# 10000000 10000000
# 100000000 100000000
# 1000000000 1000000000"""
#         output = """1 1
# 2 2
# 3 3
# 4 4
# 5 5
# 6 6
# 7 7
# 8 8
# 9 9
# 10 10"""
#         self.assertIO(input, output)


# if __name__ == "__main__":
#     unittest.main()


def resolve():
    h, w, n = map(int, input().split())
    vert = {v: 0 for _, v in enumerate(range(h))}
    horiz = {v: 0 for _, v in enumerate(range(w))}
    for i in range(n):
        a, b = map(int, input().split())
        vert[i] = a-1
        horiz[i] = b-1
    for i in range(n):
        print(vert[i], horiz[i])


resolve()
