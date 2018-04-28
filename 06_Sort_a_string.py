string = ''.join(input().split())
nums = []
letters = []
misc = []
for c in string:
    if c.isalpha():
        letters.append(c)
    elif c.isdigit():
        nums.append(c)
    else:
        misc.append(c)
nums.sort()
letters.sort()
misc.sort()
result = []
result.extend(misc)
result.extend(nums)
result.extend(letters)
print("".join(result))
