def zeros(n):
    result = 0
    p = 5
    while p <= n:
        result += n//p
        p *= 5
    return result

n = int(input())
print(n, "! has ", zeros(n), " trailing zeros.", sep="")
