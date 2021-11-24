s, t, x = map(int, input().split())

if s < t:
    print('Yes' if s < x + 0.5 < t else 'No')
else:
    if x+0.5 > s:
        print('Yes')
    elif x + 0.5 < t:
        print('Yes')
    else:
        print('No')
