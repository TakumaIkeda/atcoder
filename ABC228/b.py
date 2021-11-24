n, x = map(int, input().split())
a = list(map(int, input().split()))

already = set()

while not x in already:
    already.add(x)
    x = a[x - 1]

print(len(already))
