def asc(s):
    s = str(s)
    c = s[0]
    string = c
    length = 1
    longest = 1
    longest_string = c
    for i in range(1,len(s)):
        if int(s[i]) > int(s[i-1]):
            length += 1
            string += s[i]
        else:
            if length > longest:
                longest = length
                longest_string = string
            c = s[i]
            string = c
            length = 1
    if length > longest:
        longest = length
        longest_string = string
    return longest_string
def desc(s):
    s = str(s)
    c = s[0]
    string = c
    length = 1
    longest = 1
    longest_string = c
    for i in range(1,len(s)):
        if int(s[i]) < int(s[i-1]):
            length += 1
            string += s[i]
        else:
            if length > longest:
                longest = length
                longest_string = string
            c = s[i]
            string = c
            length = 1
    if length > longest:
        longest = length
        longest_string = string
    return longest_string
def equal(s):
    s = str(s)
    c = s[0]
    string = c
    length = 1
    longest = 1
    longest_string = c
    for i in range(1,len(s)):
        if s[i] == c:
            length += 1
            string += s[i]
        else:
            if length > longest:
                longest = length
                longest_string = string
            c = s[i]
            string = c
            length = 1
    if length > longest:
        longest = length
        longest_string = string
    return longest_string

print(asc(836926))
print(desc(2995316))
print(equal(255566))
