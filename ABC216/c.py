n = int(input())
solve = ""

while n != 0:
    if (n % 2 == 0):
        n //= 2
        solve = "B" + solve
    else:
        n -= 1
        solve = "A" + solve

print(solve)
