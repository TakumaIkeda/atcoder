A, B, K = map(int, input().split())

first = 0
for i in range(B):
    first += 2 ** i

string = ""
for i in range(K):
    if (first >> i & 1):
        string = "b" + string
    else:
        string = "a" + string

print(string)
