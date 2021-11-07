import sys

n = int(sys.stdin.readline().strip())
arrays = set()

for i in range(n):
  arrays.add(sys.stdin.readline().strip())

print(len(arrays))