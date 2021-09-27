N = int(input())

money = 0
day = 0
while(money < N):
  money += day + 1
  day += 1

print(day)