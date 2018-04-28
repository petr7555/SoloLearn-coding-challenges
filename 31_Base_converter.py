def base(exp):
    n, b = exp.split()
    n = int(n)
    b = int(b)
  
    """nb = exp.split()
    n = int(nb[0])
    b = int(nb[1]))"""

    rests = []
    while n != 0:
        rests.append(n % b)
        n = n // b
        string = ""
    for i in range(len(rests)):
        string += str(rests.pop())
    return string

print(base(input()))
