def lcm(a,b):
    div1 = prime(a,[1])
    div2 = prime(b,[1])
    common = div2[:]
    for d in div1:
        if d in div2:
            div2.remove(d)
        else:
            common.append(d)
    result = 1
    for k in common:
        result *= k
    return result

def lcm3(a,b,c):
    div1 = prime(a,[1])
    div2 = prime(b,[1])
    div3 = prime(c,[1])
    first_common = div1[:]
    for d in div2:
        if d in div1:
            div1.remove(d)
        else:
            first_common.append(d)
    second_common = first_common[:]
    for d in div3:
        if d in first_common:
            first_common.remove(d)
        else:
            second_common.append(d)
    result = 1
    for k in second_common:
        result *= k
    return result

def lcm4(a,b,c,d):
    div1 = prime(a,[1])
    div2 = prime(b,[1])
    div3 = prime(c,[1])
    div4 = prime(d,[1])
    first_common = div1[:]
    for d in div2:
        if d in div1:
            div1.remove(d)
        else:
            first_common.append(d)
    second_common = first_common[:]
    for d in div3:
        if d in first_common:
            first_common.remove(d)
        else:
            second_common.append(d)
    third_common = second_common[:]
    for d in div4:
        if d in second_common:
            second_common.remove(d)
        else:
            third_common.append(d)            
    result = 1
    for k in third_common:
        result *= k
    return result
    
def hcf(a,b):
    div1 = prime(a,[1])
    div2 = prime(b,[1])
    common = []
    for d in div1:
        if d in div2:
            common.append(d)
            div2.remove(d)            
    result = 1
    for k in common:
        result *= k
    return result

def hcf3(a,b,c):
    div1 = prime(a,[1])
    div2 = prime(b,[1])
    div3 = prime(c,[1])
    common = []
    for d in div1:
        if d in div2 and d in div3:
            common.append(d)
            div2.remove(d)
            div3.remove(d) 
    result = 1
    for k in common:
        result *= k
    return result

def hcf4(a,b,c,d):
    div1 = prime(a,[1])
    div2 = prime(b,[1])
    div3 = prime(c,[1])
    div4 = prime(d,[1])
    common = []
    for d in div1:
        if d in div2 and d in div3 and d in div4:
            common.append(d)
            div2.remove(d)
            div3.remove(d)
            div4.remove(d) 
    result = 1
    for k in common:
        result *= k
    return result
    
def prime(n, divisors):
    if n == 1:
        return divisors
    i = 2
    while n % i != 0:
        i += 1
    divisors.append(i)
    if n // i == 1:
        return divisors
    return (prime(n // i, divisors))

print(lcm(17,5))
print(hcf(0,2))
