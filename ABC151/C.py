N, M = map(int, input().split(' '))

correct = [False for i in range(N)]
wrong_count = [0 for i in range(N)]

for i in range(M):
    p, S = input().split(' ')
    p = int(p)

    if (S == 'AC'):
        correct[p - 1] = True

    if (correct[p - 1] == False and S == 'WA'):
        wrong_count[p - 1] += 1

filtered_wrong_count = []
for i in range(N):
    if (correct[i]):
        filtered_wrong_count.append(wrong_count[i])
correct_count = len(list(filter(lambda e: e, correct)))

print('{} {}'.format(str(correct_count), str(sum(filtered_wrong_count))))
