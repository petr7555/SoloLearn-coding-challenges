import math

def pronic(n):
    for i in range(n+1):
        if i*(i+1) == n:
            return True
    return False

def pronic2(n):
    x = int(math.sqrt(n))
    if x*(x+1) == n:
        return True
    return False

print(pronic2(10100))
