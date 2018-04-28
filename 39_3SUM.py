import itertools as i

def SUM(n):
    result = []
    for triplet in i.combinations(n,3):
        if sum(triplet) == 0:
            result.append(tuple(sorted(triplet)))
    return set(result)

print(SUM([-6, -1, 0, 1, 2, -1]))
