N = int(input())

A = []
B = []
lengths = {}

for i in range(N - 1):
    a, b = input().split(' ')
    A.append(int(a))
    B.append(int(b))

for i in range(N):
    city = i + 1
    length = 0
    while(city != 1):
        index = B.index(city)
        city = A[index]
        length += 1
    lengths[i + 1] = length


def isAnti(length):
    print(length)
    return length.key


lengths_sorted = sorted(lengths.items(), key=lambda x: x[1])

# a_dic = list(filter(isAnti, lengths_sorted))
# print(a_dic)


print(lengths_sorted)
