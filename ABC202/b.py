S = input()

string = ""
for i in S:
    if (i == "6"):
        string = "9" + string
    elif(i == "9"):
        string = "6" + string
    else:
        string = i + string

print(string)
