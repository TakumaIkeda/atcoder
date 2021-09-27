N = int(input())

registered_name = set()

for i in range(N):
    S = input()
    if (S in registered_name):
        continue
    print(i + 1)
    registered_name.add(S)
