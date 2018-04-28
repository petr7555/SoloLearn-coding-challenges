def armstrong(n):
    power = len(n)
    sum = 0
    for c in n:
        sum += int(c)**power
    if sum == int(n):
        return True
    return False

def all_armstrong(r):
    armstrongs = []
    for n in range(r+1):
        power = len(str(n))
        sum = 0
        for c in str(n):
            sum += int(c)**power
        if sum == n:
            armstrongs.append(n)
    return armstrongs

    
#print(armstrong(input()))
print(all_armstrong(int(input())))
