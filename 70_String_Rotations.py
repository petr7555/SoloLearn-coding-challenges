def rotate(s):
    list = []
    for i in range(len(s)):
        list.append(s[i+1:]+s[:i+1])
    return list

print(rotate("Hello"))
