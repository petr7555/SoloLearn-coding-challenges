def sieve(n):
    list = []
    for i in range(2, n+1):
        list.append(i)
    j = 0
    while j < len(list):
        p = list[j]
        x = 2
        while x*p <= list[-1]:
            if x*p in list:
                list.remove(x*p)
            x += 1
        j += 1
        
    return list

def gold(*args):
    if len(args) == 1:
        n = args[0]
        if n%2 != 0:
            return ("not an even number")
        primes = sieve(n)
        for i in range(len(primes)//2+len(primes)%2):
            if n-primes[i] in primes:
                print (str(primes[i]) + " + " + str(n-primes[i]))
    else:
        a = args[0]
        b = args[1]
        for n in range(a, b+1):
            if n%2==0:
                primes = sieve(n)
                for i in range(len(primes)//2+len(primes)%2):
                    if n-primes[i] in primes:
                        print (str(n) + ": " + str(primes[i]) + " + " + str(n-primes[i]))
gold(32)
gold(4,8)
