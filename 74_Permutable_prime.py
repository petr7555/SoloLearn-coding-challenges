from itertools import permutations
def isPrime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    
    return True

def permutable(n):
    perms = list(set((permutations(str(n)))))
    nums = []
    # parse
    for perm in perms:
        num = ""
        for i in range(len(perm)):
            num += perm[i]
        nums.append(int(num))
    for num in nums:
        if not isPrime(num):
            return False
    return True

print(permutable(79))
print(permutable(127))
print(permutable(337))
