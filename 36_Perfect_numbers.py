def perfect(n):
    propers = []
    for i in range(1,n):
        if n % i == 0:
            propers.append(i)
    if sum(propers) == n:
        return True, propers
    return False, propers

def all_perfect(n):
    all = []
    for j in range(6,n+1): 
        propers = []
        for i in range(1,j):
            if j % i == 0:
                propers.append(i)
        if sum(propers) == j:
            all.append((j, propers))
    return all

print(all_perfect(500))
