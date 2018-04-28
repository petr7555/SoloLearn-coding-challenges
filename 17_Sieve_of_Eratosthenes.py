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

print(sieve(100))
