import itertools

def guitar(G,S):
    for i in range(1,len(S)+1):
        for subset in itertools.combinations(S, i):
            if sum(subset) == G:
                return list(subset)
    return False


print(guitar(24,[12,1,61,5,9,2]))
print(guitar(25,[12,1,61,5,9,2]))
