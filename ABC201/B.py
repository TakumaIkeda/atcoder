N = int(input())

name1 = ""
height1 = 0

name2 = ""
height2 = 0

for i in range(N):
  S, T = input().split()
  T = int(T)

  if (T > height1):
    height2 = height1
    name2 = name1
    height1 = T
    name1 = S
  elif (T > height2):
    height2 = T
    name2 = S

print(name2)