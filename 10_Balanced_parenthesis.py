string = input()
left = 0
right = 0
escape = 0
for i in range(len(string)):
    if i == 0:
        if string[i] == "(": 
            left += 1
        if string[i] == ")":
            right += 1
    elif string[i-1] != "\\":
        if string[i] == "(": 
            left += 1
        if string[i] == ")":
            right += 1
if left == right:
    print("valid")
else:
    print("invalid")
