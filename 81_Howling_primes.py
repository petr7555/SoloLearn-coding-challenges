def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    
    return True

def howl(n):
    if not isPrime(n):
        return False
    dsum = sum(map(int, list(str(n))))
    if isPrime(dsum):
        return True
    return False


print(howl(113))
print(howl(89))
print(howl(19))
