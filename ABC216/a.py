x, y = map(int, input().split("."))
if (0 <= y and y <= 2):
    print("{}-".format(x))
elif (3 <= y and y <= 6):
    print("{}".format(x))
else:
    print("{}+".format(x))
