N = int(input())
A = input().split(' ')
A = list(map(lambda e: int(e), A))
count = 0
while(all(map(lambda e: e % 2 == 0, A))):
    A = list(map(lambda e: e / 2, A))
    count += 1
print(count)
