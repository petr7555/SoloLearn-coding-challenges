def expression(n1, op, n2):
    #n1 is variable    
    if n1[0].isalpha():
        n1 = variables[n1]
    #no expression
    if n2 == None:
        return n1
    #n2 is variable
    if n2[0].isalpha():
        n2 = variables[n2]
    return eval(str(n1) + op + str(n2))

with open("source_code.txt", "r") as source:

    """read commands"""
    lines = list(map(str.strip, source.read().split(";")[:-1]))

    variables = {}
    for command in lines:
        words = command.split()
        """declaring variables"""
        if words[0] == "svar":
            variables[words[1]] = 0
        """assignment operator"""
        if words[1] == "=":
            #assign string
            if words[2][0] == "\"":
                variables[words[0]] = " ".join(words[2:])[1:-1]
            #assign result of expression
            else:
                variables[words[0]] = expression(words[2], words[3] if len(words) > 3 else None, words[4] if len(words) > 4 else None)
        """print operator"""
        if words[0] == "print":
            #print string
            if words[1][0] == "\"":
                print(" ".join(words[1:])[1:-1])
            #print result of expression
            else:
                print(expression(words[1], words[2] if len(words) > 2 else None, words[3] if len(words) > 3 else None))
