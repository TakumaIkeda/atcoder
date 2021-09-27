n = int(input())
prev = int(input())
for i in range(n - 1):
    a = int(input())
    if (a == prev):
        print("stay")
    if (a < prev):
        print('down {}'.format(prev - a))
    if (a > prev):
        print('up {}'.format(a - prev))
    prev = a
