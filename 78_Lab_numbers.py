import math
def isPrime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    
    return True

def lab(n):
    for i in range(1, math.floor(n**0.5)+1):
        if n % i == 0 and n % (i**2) == 0 and isPrime(i):
            return True
    return False

def statistics(a,b):
    counter = 0
    for i in range(a,b):
        if lab(i):
            counter += 1
    return (round(counter/(b-a),3))

print(statistics(1,100))
