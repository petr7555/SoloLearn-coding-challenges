from itertools import permutations as p

def MinSum(x):
    l = len(x)
    lst = [sum(j[i]*j[i+1] for i in range(l - 1)) for j in p(x)]
    print("Minimum sum is", min(lst), "for\n", list(p(x))[lst.index(min(lst))])

inp = list(map(int,input().split()))
MinSum(inp)
