import sys

x = int(sys.stdin.readline().strip())

print('Yes' if x % 100 == 0 and x >= 100 else 'No')
