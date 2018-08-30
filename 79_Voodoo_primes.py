def isPrime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    
    return True

def voodoo(n):
    if not isPrime(n):
        return False
    if str(n) in str(1/n):
        return True, str(1/n)
    return False

print(voodoo(3))
print(voodoo(7))
print(voodoo(11))
