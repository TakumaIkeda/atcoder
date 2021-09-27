def isOdd(product):
    return product % 2 == 1


a, b = input().split(' ')
a = int(a)
b = int(b)

if (isOdd(a * b)):
    print('Odd')
else:
    print('Even')
