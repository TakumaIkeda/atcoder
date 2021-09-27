x = input()

if (x[0] == x[1] and x[1] == x[2] and x[2] == x[3]):
  print('Weak')
elif (str(int(x[0]) + 1)[-1] == x[1] and str(int(x[1]) + 1)[-1] == x[2] and str(int(x[2]) + 1)[-1] == x[3]):
  print('Weak')
else:
  print('Strong')