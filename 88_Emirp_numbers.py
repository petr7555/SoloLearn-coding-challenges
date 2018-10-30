def isPrime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    
    return True

def emirp(n):
    if isPrime(n):
        if isPrime(int(str(n)[::-1])):
            return True
    return False
for i in range(10):
    print(emirp(int(input())))
