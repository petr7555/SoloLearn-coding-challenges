import math

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    
    return True


def mers(n):
    if not isPrime(n):
        return False
    n += 1
    if math.log2(n).is_integer():
        return True
    return False


print(mers(3))
print(mers(31))
print(mers(17))
