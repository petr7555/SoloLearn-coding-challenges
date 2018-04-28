def reciprocal(string):
    reversed = []
    for c in string:
        if c.isalpha():
            if c.upper() == c:
                order = ord(c) - ord("A")
                reversed.append(chr(ord("Z") - order))
            else:
                order = ord(c) - ord("a")
                reversed.append(chr(ord("z") - order))
        else: reversed.append(c)    
    return "".join(reversed)

print(reciprocal(input()))
