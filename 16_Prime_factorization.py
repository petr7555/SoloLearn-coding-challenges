divisors = []

def prime(n):
    if n == 1:
        string = "2^0"
        return string
    i = 2
    while n % i != 0:
        i += 1
    divisors.append(i)
    if n // i == 1:
        return toString(divisors)
    return (prime(n // i))

def toString(divisors):
    dict = {}
    for num in divisors:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    string = ""
    for pair in dict:
        string += str(pair) + "^" + str(dict[pair]) + "*"
    return string[:-1]


print (prime(int(input())))
