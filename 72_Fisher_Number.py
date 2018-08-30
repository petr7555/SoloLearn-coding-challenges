def fish(n):
    divisors = []
    string = ""
    m = 1
    for i in range(1, n+1):
        if n%i == 0:
            m *= i
            divisors.append(i)
    for divisor in divisors:
            string += str(divisor) + " x "
    if n**3 == m:
        return ("true ("+str(n)+"^3 = "+string[:-3]+")")
    else:
        return ("false ("+str(n)+"^3 != "+string[:-3]+")")
    
#print all Fisher numbers up to 100
for i in range(1,100):
    if fish(i)[:4]=="true":
        print(fish(i))
