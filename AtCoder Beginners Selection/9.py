from math import floor


def getNumberOfBill(N, Y):
    for i in range(floor(Y / 10000) + 1):
        if (Y - i * 10000 == 0 and i == N):
            return [i, 0, 0]
        for j in range(floor((Y - i * 10000) / 5000 + 1)):
            if (Y - i * 10000 - j * 5000 == 0 and i + j == N):
                return [i, j, int((Y - i * 10000 - j * 5000) / 1000)]
            k = int((Y - i * 10000 - j * 5000) / 1000)
            if (i + j + k == N):
                return [i, j, k]

    return [-1, -1, -1]


N, Y = input().split(' ')
N = int(N)
Y = int(Y)

bill = getNumberOfBill(N, Y)

print('{} {} {}'.format(bill[0], bill[1], bill[2]))
