def comp(string):
    compressed = ""
    stack = []
    for i in range(len(string)):
        count = 0
        if len(stack) == 0 or string[i] in stack:
            stack.append(string[i])
        else:
            while len(stack) != 0:
                char = stack.pop()
                count += 1
            stack.append(string[i])
            compressed += char
            if count > 1:
                compressed += str(count)
    count = 0
    while len(stack) != 0:
        char = stack.pop()
        count += 1
    compressed += char
    if count > 1:
        compressed += str(count)
    
    return compressed

print(comp(input()))
