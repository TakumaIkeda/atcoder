s = input()
nums = []

try:
    for i in range(len(s)):
        nums.append(int(s[i]))
except ValueError:
    print('error')
    exit()

print((nums[0] * 100 + nums[1] * 10 + nums[2]) * 2)
