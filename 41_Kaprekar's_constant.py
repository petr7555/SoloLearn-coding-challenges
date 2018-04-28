dict = {}
def kap(n):
    global dict
    
    if n == 6174:
        return True
    
    n = str(n)
    asc = []
    desc = []    
    
    for c in n:
        asc.append(c)
    asc = sorted(asc)
    desc = sorted(asc, reverse=True)
    larger = int("".join(desc))
    smaller = int("".join(asc))
    result = larger - smaller
    
    string = str(larger) + " - " + str(smaller) + " = " + str(result)
    if dict.get(result) == 1:
        return False
    else:
        dict[result] = 1
    return kap(result)

def all_kap():
    global dict
    c = 0
    for i in range(0,9999):
        dict = {}
        if kap(i):
            c += 1
    return c
        
print(all_kap())
