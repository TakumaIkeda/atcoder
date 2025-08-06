n, k = map(int, input().split())
k = str(k)
k_re = k[::-1]

k = str(min(int(k), int(k_re)))
