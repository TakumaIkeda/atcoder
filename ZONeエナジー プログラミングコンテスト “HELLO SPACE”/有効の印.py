N, D, H = input().split(' ')
N = int(N)
D = int(D)
H = int(H)

h = 0.0

for i in range(N):
    d_i, h_i = input().split(' ')
    d_i = int(d_i)
    h_i = int(h_i)

    height = (H / D - h_i / d_i) / (1 / D - 1 / d_i)

    if (height > h):
        h = height


print(h)
