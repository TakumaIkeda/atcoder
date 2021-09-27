N = int(input())

arr = []

for i in range(N):
  t, l, r = map(int, input().split())
  arr.append([t, l, r])

count = 0
for i in range(len(arr)):
  j = i + 1
  while j < len(arr):
    if (arr[j][1] < arr[i][1] and arr[i][1] < arr[j][2]):
      count += 1
    elif(arr[j][1] < arr[i][2] and arr[i][2] < arr[j][2]):
      count += 1
    elif(arr[j][1] == arr[i][1] or arr[j][2] == arr[i][2]):
      count += 1
    elif (arr[i][1] < arr[j][1] and arr[j][1] < arr[i][2]):
      count += 1
    elif (arr[i][1] < arr[j][2] and arr[j][2] < arr[i][2]):
      count += 1
    elif(arr[j][2] == arr[i][1] and ((arr[j][0] == 1 or arr[j][0] == 3) and (arr[i][0] == 1 or arr[i][0] == 2))):
      count += 1
    elif(arr[i][2] == arr[j][1] and ((arr[i][0] == 1 or arr[i][0] == 3) and (arr[j][0] == 1 or arr[j][0] == 2))):
      count += 1
    j += 1

print(count)