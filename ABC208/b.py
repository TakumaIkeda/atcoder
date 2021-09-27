from math import factorial
# from math import

P = int(input())
ONE = factorial(1)
TWO = factorial(2)
THREE = factorial(3)
FOUR = factorial(4)
FIVE = factorial(5)
SIX = factorial(6)
SEVEN = factorial(7)
EIGHT = factorial(8)
NINE = factorial(9)
TEN = factorial(10)

rest = P

count = 0

while (rest != 0):
  count += 1
  if rest >= TEN:
    rest -= TEN
    continue
  if rest >= NINE:
    rest -= NINE
    continue
  if rest>= EIGHT:
    rest -= EIGHT
    continue
  if rest >= SEVEN:
    rest -= SEVEN
    continue
  if rest >= SIX:
    rest -= SIX
    continue
  if rest >= FIVE:
    rest -= FIVE
    continue
  if rest >= FOUR:
    rest -= FOUR
    continue
  if rest >= THREE:
    rest -= THREE
    continue
  if rest >= TWO:
    rest -= TWO
    continue
  if rest >= ONE:
    rest -= ONE
    continue
print(count)