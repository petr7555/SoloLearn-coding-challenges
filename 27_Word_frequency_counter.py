def freq(string, substring):
    count = 0
    
    new_string = []
    for i in range(len(string)):
        if string[i].isalpha() == False:
            new_string.append(" ")
        else:
            new_string.append(string[i])
    words = "".join(new_string).lower().split()
    
    while substring.lower() in words:
        words.remove(substring.lower())
        count += 1
    return count

print(freq("this is a sample text", "is"))
print(freq("Some. long only some.text with some words", "some"))
