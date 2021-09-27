H, W = map(int, input().split(' '))

count = 0

count += (H // 2) * (W // 2)

if (H % 2 == 1):
    count += W // 2

if (W % 2 == 1):
    count += H // 2

if (H % 2 == 1 and W % 2 == 1):
    count += 1

print(count)
